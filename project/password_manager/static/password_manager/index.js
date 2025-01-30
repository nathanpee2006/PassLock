document.addEventListener('DOMContentLoaded', function() {

    const select = document.querySelector('select');
    select.onchange = () => {
        let type = select.value;

        const form = document.querySelector('form');
        form.setAttribute('action', `/add/${type}`)

        const formFields = document.getElementById('form-fields');
        formFields.innerHTML = '';

        getForm(type);
    }; 

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
        }
        else {
            document.getElementById('form-fields').innerHTML = json.error;
        }
    } catch (error) {
        console.error(error.message);
    }
}

