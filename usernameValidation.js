//A simple username validation for Codrebyte.com
// Have the function CodelandUsernameValidation(str) take the
// str parameter being passed and determine if the string is a valid 
// username according to the following rules:

// 1. The username is between 4 and 25 characters.
// 2. It must start with a letter.
// 3. It can only contain letters, numbers, and the underscore character.
// 4. It cannot end with an underscore character.

// If the username is valid then your program should return the string true, otherwise return the string false.

function CodelandUsernameValidation(str) {
    const validate = true;
    if (str.length > 4 && str.length < 25) {
        if (/^[a-zA-Z0-9]/.test(str.charAt(0))){
            if (/^[a-zA-Z0-9_]+$/.test(str) && str.charAt(str.length-1) !== '_'){
                return validate;
            }
        }
    }
    return !validate;
}
console.log(CodelandUsernameValidation(readline()));
