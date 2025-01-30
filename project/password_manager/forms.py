from django.forms import ModelForm, PasswordInput 
from password_manager.models import Login, Card, PIN, SecureNote


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ["name", "username", "password", "website", "note"]
        widgets = {
            "password": PasswordInput()  
        }


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["name", "cardholder", "number", "expiration_date", "cvv"]
        widgets = {
            "number": PasswordInput(),
            "cvv": PasswordInput()
        }

class PINForm(ModelForm):
    class Meta:
        model = PIN
        fields = ["name", "code", "note"]
        widgets = { 
            "code": PasswordInput()
        }

class SecureNoteForm(ModelForm):
   class Meta:
       model = SecureNote 
       fields = ["name", "notes"]

