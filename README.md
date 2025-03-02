# Password Manager

## Overview

When using applications in the internet, most people tend to reuse simple passwords to easily authenticate themselves. However, this poses a security risk as an attacker may be able to use the same password to login into the other accounts of the same user. Even I find myself doing this a lot. To prevent this from happening, passwords need to be complex, long, and hard-to-guess. At the cost of increased security, convenience takes a toll. 

Because of this, I decided to build a password manager web application called **PassLock** for my CS50W Capstone Project. This is designed to securely store and manage sensitive credentials in a centralized location. 

### Key Features:
* Encryption keys for encrypting and decrypting data 
* Create, View, Edit, and Delete credentials
* Encrypted credentials stored in a database
* Decrypt credentials when needed for viewing
* Organized and Favorited Credentials
* Password Generator and Health Checker
* Copy-Credential-to-Clipboard and Toggle Visibility

### Tech Stack:
* HTML
* CSS (Bootstrap)
* Javascript
* Python (Django)
* SQLite DB

## Distinctiveness and Complexity

I believe my project is distinct and complex because:

* It implements AES symmetric cryptography, wherein a Data Encryption Key (DEK) is generated based from a user's master password, a randomly generated salt, and a Key Derivation Function (KDF) called *scrypt*. This is the key that the user only has access to encrypt and decrypt their credentials.

* The concept of **Envelope Encryption** is also utilised. This uses another key called a Key Encryption Key (KEK). This KEK is used to encrypt and decrypt the DEK, which is used for encrypting and decrypting the user's sensitive information. This means a malicious threat actor will not be able to decrypt the credentials without the KEK since the DEK is encrypted. Only the user has access to the DEK and is able to decrypt the DEK with the KEK. [To learn more about Envelope Encryption click here.](https://cloud.google.com/kms/docs/envelope-encryption)

* It uses an external Python library called **PyCryptodome**, which contains functions for encrypting and decrypting data. I had to read the documentation, to understand what it was doing, to implement it in the codebase. 

* The password manager web app stores the encrypted DEK in the session and decrypts it when the user views a credential. To increase security, sessions have a time limit. When the time limit is reached, the user is logged out and the session data is flushed.  

* It utilises JavaScript fetch() from the frontend to retrieve data from the backend such as Django Forms and credentials from the database. It was also used to update data from the frontend (i.e. favoriting and unfavoriting a credential).

* It contains complex CRUD operations on credentials. 
    * CREATING a credential involves rendering the correct Django Form to properly store credentials in the right place. (i.e. if a user selects 'Login' as the type of credential to store, a LoginForm is rendered and and the login credentials are saved in the Login model. Before storage the DEK is used to encrypt the data.)
    * READING a credential involves retrieving the encrypted credentials from the database and rendering the data in form fields. Before being placed in the fields, the selected credential is decrypted using the DEK. 
    * UPDATING a credential involves checking the edited fields. For example, everytime a user edits a credential the backend checks whether specific fields where edited. If the password field was not changed, the backend knows this and does not update and re-encrypt the password. If the password was changed, it updates the field and re-encrypts the password. This is done to reduce unnecesary performance overhead.
    * DELETING a credential involves identifying the credential the user selected and removing it from the database.

* A password genarator creates a random password everytime a user changes the selected parameters such as the length and type of characters. 

* An external API from [Enzoic](https://docs.enzoic.com/enzoic-api-developer-documentation/password-strength-meter) is utilised. It checks the strength of a password and identifies if it has been publicly exposed in the internet.

* Event listeners were used to run certain functions when an event was triggered. (i.e. if a user clicked an copy-to-clipboard icon, it would copy the selected credential into their clipboard.)

## File Structure

* **password-manager/** 
    * `README.md` - *documentation*
    * `requirements.txt` - *dependencies required to run application*
    * **project/**
        * **password-manager/** - *app directory*      
            * **static/password_manager/** - *contains JavaScript and CSS files*
                * `index.js` *contains logic to dynamically fetch specific Django form based on user's selected option. It also contains code to view, edit, and delete credentials. Furthermore, it has the feature to toggle credential visibility and to copy it to clipboard. It also applies the Enzoic API's password strength meter to password fields.*
                * `favorites.js` - *logic to favorite and unfavorite credential via fetch()*
                * `password-generator.js` - *logic to generate a random password to an input field based on the chosen parameters (e.g. length, excluding symbols in password)*
                * `styles.css` - *contains styling and mobile-responsive configurations*
            * **templates/password_manager/** - *contains HTML files*
                * `favorites.html` - *page that contains favorited credentials*
                * `index.html` - *page to view, add, edit, delete credentials*
                * `layout.html` - *parent template*
                * `login.html` - *login page*
                * `password-generator.html` - *page that generates a password for a user*
                * `password-health-check.html` -  *page that checks the strength of password and identifies if it is publicly exposed* 
                * `register.html` - *register page*
                * `type.html` - *page that shows credential based on selected type (e.g. if user selects 'Card', they will only see all their debit/credit card credentials in that page)*
            * `admin.py` - *admin view configuration*
            * `forms.py` - *contains Django ModelForms*
            * `models.py` - *contains Models*
            * `urls.py` - *contains url patterns*
            * `utils.py` - *reusable helper functions. (e.g. generating keys, encrypting and decrypting data)*
            * `views.py` - *contains view functions that handle backend logic*
        * **project/** - *project directory*
            * `settings.py` - *configuration settings for DB, apps, middleware, session, etc.*
            * `urls.py` - *url configuration*
        * `db.sqlite3` - *database that stores encrypted credentials*
        * `manage.py` - *commands ran by Django (running local development server and applying migrations)*
    

## How to Run
Provide clear instructions on how to set up and run your project. Example:
1. Clone the repository:
    ```sh
    git clone https://github.com/nathanpee2006/password-manager.git
    cd password-manager/project 
    ```
2. Install dependencies
    
    ```sh
    python -m venv env

    If using Windows:
    env/Scripts/activate

    If using Linux:
    source env/bin/activate

    pip install -r requirements.txt
    ```
3. Run the application
    ```sh
    python manage.py runserver
    ```
4. Open your browser and visit
    ```
    http://127.0.0.1:8000/
    ```

## Additional Information
In a `.env` file, be sure to add a Key Encryption Key before using the web application. Without this, it **will not work** properly.

To do add the Key Encryption Key (KEK):
1. Create a `.env` file in the same directory as `manage.py`.
2. Run the Python script. 
    ```sh
    python generate_KEK.py
    ```
3. In the terminal copy-paste the KEK into the `.env` file into the following format.
    ```
    KEK='EAu3CXtnMm2OgsTCy6NbGQ==' # This an example only. DO NOT use this.
    ```