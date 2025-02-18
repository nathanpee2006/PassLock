document.addEventListener('DOMContentLoaded', function() {

    window.onload = generatePassword;

    const generatePasswordBtn = document.getElementById('btn-generate-password');
    generatePasswordBtn.addEventListener('click', () => generatePassword());

    const slider = document.getElementById('length');
    slider.addEventListener('input', generatePassword);

    const numberIndicator = document.getElementById('number');
    numberIndicator.addEventListener('input', generatePassword);

    document.querySelectorAll('input[type=checkbox]').forEach((checkbox) => {
        checkbox.checked = true;
        checkbox.addEventListener('click', generatePassword);
        checkbox.addEventListener('change', (event) => {
            const tickedCheckboxes = document.querySelectorAll('input[type=checkbox]:checked');
            if (tickedCheckboxes.length === 0 && !event.target.checked) {
                event.target.checked = true;
            }
            generatePassword();
        })
    })
})

function generatePassword() {
    const char_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const char_lower = 'abcdefghijklmnopqrstuvwxyz';
    const numbers = '0123456789';
    const char_symbol = '!@#$%^&*()-_=+[]{}|;:,.<>?';
    
    const hasUpper = document.getElementById('uppercase').checked;
    const hasLower = document.getElementById('lowercase').checked;
    const hasNumbers = document.getElementById('numbers').checked;
    const hasSymbols = document.getElementById('symbols').checked;
    let selectedChars = '';
    if (hasUpper) {
        selectedChars += char_upper;
    }
    if (hasLower) {
        selectedChars += char_lower;
    }
    if (hasNumbers) {
        selectedChars += numbers;
    }
    if (hasSymbols) {
        selectedChars += char_symbol;
    }

    let length = document.getElementById('length').value; 
    let result = '';
    for (let i = 0; i < length; i++) {
        result += selectedChars.charAt(Math.floor(Math.random() * selectedChars.length))
    }

    document.getElementById('generated-password').value = result;
}
