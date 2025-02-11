import { favorite } from "./favorites.js";
import { unfavorite } from "./favorites.js";

document.addEventListener('DOMContentLoaded', function () {

    if (document.querySelector('select') !== null) {
        const select = document.querySelector('select');
        select.onchange = () => {
            let type = select.value;

            const form = document.querySelector('form');
            form.setAttribute('action', `/add/${type}`)

            const formFields = document.getElementById('form-fields');
            formFields.innerHTML = '';

            getForm(type);
        }
    }


    const tableRows = document.querySelectorAll('.table-row');
    tableRows.forEach((tableRow) => {

        let type = tableRow.dataset.type;
        let uuid = tableRow.dataset.uuid;

        const tableRowData = tableRow.querySelectorAll('td:not(:first-child)');
        tableRowData.forEach((tableData) => {
            tableData.addEventListener('click', () => {
                getUserCredentials(type, uuid);
                window.location.href = '#offcanvasScrolling';
            })
        })
    })


    document.getElementById('offcanvas-btn-close').addEventListener('click', () => {
        if (window.location.hash = '#offcanvasScrolling') {
            window.location.href = '/';
        }
        if (window.location.href.includes('/favorites#offcanvasScrolling')) {
            window.location.href = '/favorites';
        }
    })

});


async function getForm(type) {
    const params = new URLSearchParams({
        'type': type
    })

    try {
        const response = await fetch(`/get-form?${params}`);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        if (json.form) {
            document.getElementById('form-fields').innerHTML = json.form;

            if (document.getElementById('form-fields').querySelector('input[name=password]')) {
                const passwordField = document.getElementById('form-fields').querySelector('input[name=password]'); 
                passwordField.type = 'password';
                toggleVisibility(passwordField)
            }
            if (document.getElementById('form-fields').querySelector('input[name=number]') && document.getElementById('form-fields').querySelector('input[name=cvv]')) {
                const numberField = document.getElementById('form-fields').querySelector('input[name=number]');
                numberField.type = 'password'; 
                toggleVisibility(numberField);
                const cvvField = document.getElementById('form-fields').querySelector('input[name=cvv]');
                cvvField.type = 'password';
                toggleVisibility(cvvField);
            }
            if (document.getElementById('form-fields').querySelector('input[name=code]')) {
                const codeField = document.getElementById('form-fields').querySelector('input[name=code]');
                codeField.type = 'password';
                toggleVisibility(codeField);
            }
        }
        else {
            document.getElementById('form-fields').innerHTML = json.error;
        }
    } catch (error) {
        console.error(error.message);
    }
}


async function getUserCredentials(type, uuid) {

    console.log(type, uuid);
    const csrftoken = document.getElementById('credential-form').querySelector('input[name=csrfmiddlewaretoken]').value;

    try {
        const response = await fetch('/get-credentials', {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            method: 'POST',
            body: JSON.stringify({
                type: type,
                uuid: uuid
            }),
            mode: 'same-origin'
        })
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const json = await response.json();
        console.log(json);
        if (json.form) {
            document.getElementById('credential-form-fields').innerHTML = json.form;

            if (document.querySelector('.offcanvas').querySelector('input[name=password]')) {
                const passwordField = document.querySelector('.offcanvas').querySelector('input[name=password]'); 
                passwordField.type = 'password';
                toggleVisibility(passwordField)
            }
            if (document.querySelector('.offcanvas').querySelector('input[name=number]') && document.querySelector('.offcanvas').querySelector('input[name=cvv]')) {
                const numberField = document.querySelector('.offcanvas').querySelector('input[name=number]');
                numberField.type = 'password'; 
                toggleVisibility(numberField);
                const cvvField = document.querySelector('.offcanvas').querySelector('input[name=cvv]');
                cvvField.type = 'password';
                toggleVisibility(cvvField);
            }if (document.querySelector('.offcanvas').querySelector('input[name=code]')) {
                const codeField = document.querySelector('.offcanvas').querySelector('input[name=code]');
                codeField.type = 'password';
                toggleVisibility(codeField);
            }

            let name = document.querySelector('.offcanvas').querySelector('input[name=name]').value;
            document.querySelector('.offcanvas-title').innerHTML = name;

            const favoriteButton = document.createElement('button');
            favoriteButton.className = 'favorite-btn';
            if (!json.is_favorited) {
                favoriteButton.innerHTML = '<i class="bi bi-star"></i>';
            } else {
                favoriteButton.innerHTML = '<i class="bi bi-star-fill favorite"></i>';
            }

            document.querySelector('.offcanvas-title').insertAdjacentElement("afterend", favoriteButton);
            favoriteButton.addEventListener('click', () => {
                if (favoriteButton.firstChild.className === 'bi bi-star') {
                    favorite(type, uuid);
                    favoriteButton.firstChild.className = 'bi bi-star-fill favorite';
                } else {
                    unfavorite(type, uuid);
                    favoriteButton.firstChild.className = 'bi bi-star';
                }
            })
        }
        else {
            document.getElementById('credential-form-fields').innerHTML = json.error;
        }
    } catch (error) {
        console.error(error.message);
    }
}


function toggleVisibility(field) {
    const toggleVisibilityBtn = document.createElement('button');
    toggleVisibilityBtn.className = 'eye-icon';
    toggleVisibilityBtn.type = 'button';
    toggleVisibilityBtn.innerHTML = '<i class="bi bi-eye"></i>';

    field.insertAdjacentElement("afterend", toggleVisibilityBtn)

    toggleVisibilityBtn.addEventListener('click', () => {
        if (toggleVisibilityBtn.innerHTML === '<i class="bi bi-eye"></i>') {
            field.type = 'text';
            toggleVisibilityBtn.innerHTML = '<i class="bi bi-eye-slash"></i>';
        } else {
            field.type = 'password';
            toggleVisibilityBtn.innerHTML = '<i class="bi bi-eye"></i>';
        }
    })
}