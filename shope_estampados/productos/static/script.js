mostrarPassword('password1', 'mostrarPassword1');
 mostrarPassword('password2', 'mostrarPassword2');

function mostrarPassword(passwordInputId, checkboxId) {
    var passwordInput = document.getElementById(passwordInputId);
    var mostrarPasswordCheckbox = document.getElementById(checkboxId);

    mostrarPasswordCheckbox.addEventListener('change', function() {
        if (this.checked) {
            passwordInput.type = 'text';
        } else {
            passwordInput.type = 'password';
        }
    });
}

function mostrarPasswordInicio() {
    var passwordInput = document.getElementById("password");
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}