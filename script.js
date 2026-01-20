function togglePassword(){
     var passwordInput = document.getElementById("password");
            var toggleButton = document.querySelector("button");
            if (passwordInput.type === "password") {
                passwordInput.type = "text";
                toggleButton.textContent = "HIDE";
            } 
            else {
                passwordInput.type = "password";
                toggleButton.textContent = "SHOW";
            }
}