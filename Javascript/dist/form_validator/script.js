document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#myForm');
    const nameInput = document.querySelector('#name');
    const emailInput = document.querySelector('#email');
    const messageInput = document.querySelector('#message');
    const submitButton = document.querySelector('#submit');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        updateForm();
    });

    function updateForm() {
        const name = nameInput.value;
        const email = emailInput.value;
        const message = messageInput.value;

        if (validateForm(name, email, message)) {
            console.log('Form submitted successfully!');
            // Perform form submission actions here
        } else {
            console.log('Form validation failed.');
        }
    }

    function validateForm(name, email, message) {
        if (name === '' || email === '' || message === '') {
            alert('All fields are required.');
            return false;
        }
        if (!validateEmail(email)) {
            alert('Please enter a valid email address.');
            return false;
        }
        return true;
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }
});