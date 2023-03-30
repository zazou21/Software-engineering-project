//each field has an expected input from the team so we check if the input is valid
//fields cannot be empty when the user press the button
//error messages are displayed to help users understand
const form = document.getElementById("form");
const email = document.getElementById("email");
const submit = document.getElementById("submit");


//adding classes to be used later to add error messages and formmatting the form colors
function showError(input, message) {
    const formControl = input.parentElement;
    formControl.classList.remove("success");
    formControl.classList.add("error");
    const error = formControl.querySelector(".errorMessage");
    error.innerText = message;
}

function showSuccess(input) {
    const formControl = input.parentElement;
    formControl.classList.remove("error");
    formControl.classList.add("success");
    const error = formControl.querySelector(".errorMessage");
    error.innerText = "";
}

function checkEmail(input) {
    const emailValue = input.value.trim();
    const emailformat = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;//email format
    if (emailformat.test(emailValue)) {
        showSuccess(input);
    } else {
        showError(input, "Email is not valid");
    }
}


function checkLength(input, min, max) {
    if (input.value.length < min) {
        showError(
            input,
            `${getFieldName(input)} must be at least ${min} characters`
        );
    } else if (input.value.length > max) {
        showError(
            input,
            `${getFieldName(input)} must be less than ${max} characters`
        );
    } else {
        showSuccess(input);
    }
}

//to make each error start with the data field name"id"
function getFieldName(input) {
    return input.id.charAt(0).toUpperCase() + input.id.slice(1);
}

//trigger the functions after the user types in the form fields and then leaves the field(blur)
email.addEventListener("blur", function () {
    checkEmail(email);
});
password.addEventListener("blur", function () {
    checkLength(password, 8, 30);
});

submit.addEventListener("click", function (event) {
    event.preventDefault();

    //check if fields are empty
    const requiredFields = [email, password];
    let isEmpty = false;
    requiredFields.forEach(function (input) {
        if (input.value.trim() === "") {
            showError(input, `${getFieldName(input)} is required`);
            isEmpty = true;
        }
    });
    if (isEmpty) {
        return;
    }
    //trigger the functions when the user press the button
    checkEmail(email);
    checkLength(password, 8, 30);
});
