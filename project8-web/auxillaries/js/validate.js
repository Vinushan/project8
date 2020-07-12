
function ValidateSellerCreate(){
    var PhoneNumber = document.forms["seller-create"]["phone_number"];
    var Email = document.forms["seller-create"]["email"];
    var Password = document.forms["seller-create"]["password"];
    var ConfirmPassword = document.forms["seller-create"]["confirm_password"];

    var RegexPhone = /^\d{10}$/;
    var RegexEmail = /^\S+@\S+.\S+$/;
    var RegexPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;

    if (!(PhoneNumber.value.match(RegexPhone))){
        alert("Please enter a valid contact number")
        PhoneNumber.focus()
        return false
    }

    if (!(Email.value.match(RegexEmail))){
        alert("Please enter a valid email address")
        Email.focus()
        return false
    }

    if (!(Password.value.match(RegexPassword))){
        alert("Password should be between 8 to 15 characters which contain at least one \
        lowercase letter, one uppercase letter, one numeric digit, and one special character")
        Password.focus()
        return false
    }    

    if (!(Password.value == ConfirmPassword.value)){
        alert("Password and Confirmation Password does not match")
        ConfirmPassword.focus()
        return false
    } 

    return true
}


function OnlyNumber(key) { 
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    if (numbers.includes(key)){
        return true
    } else {
        return false
    }
} 