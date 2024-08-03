var generatePassword = function(length, field_name, form_id){
    var form = document.getElementById(form_id);
    var passwordField = form.elements[field_name]

    newPassword = '';
    var possibleCharacters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    for(var i = 0; i<length; i++) {
        var randValue = Math.floor(Math.random() * possibleCharacters.length);
        newPassword += possibleCharacters.charAt(randValue);
    }

    if (passwordField) {
        passwordField.value = newPassword;
    } else {
        console.error("Password field not found in the form.");
    }

    console.log(passwordField.value);
    return passwordField.value;
}
