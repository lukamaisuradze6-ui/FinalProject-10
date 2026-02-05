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
};



let subjects = document.getElementById("subjects");
let popup = document.getElementById("popupp");

popup.style.display = 'none';


subjects.onclick = function(){
if (popup.style.display == 'none'){
    popup.style.display = 'flex';
}else{
    popup.style.display = 'none';
};
};

let close = document.getElementById("close");

close.onclick = function(){
    popup.style.display ='none';
};


let subject = document.getElementById("choice");
let subject2 = document.getElementById("choice2");
let subject3 = document.getElementById("choice3");



let fr = document.getElementById("fr");
let yup = document.getElementById("YUP")
let hellno = document.getElementById("HELLNAH");


subject.onclick = function(){
    if (this.style.backgroundColor === 'rgb(20, 237, 0)') {
        console.log("");
        

    } else {
        this.style.backgroundColor = 'rgb(20, 237, 0)';
        
        

    };
};
subject2.onclick = function(){
    if (this.style.backgroundColor === 'rgb(20, 237, 0)') {
       console.log("");
        
    } else {
        this.style.backgroundColor = 'rgb(20, 237, 0)';
        
    };
};
subject3.onclick = function(){
    if (this.style.backgroundColor === 'rgb(20, 237, 0)') {
        console.log("");
        
    } else {
        this.style.backgroundColor = 'rgb(20, 237, 0)';
        
    };
};



hellno.onclick = function(){
    if ((subject|| subject2 || subject3).style.backgroundColor ==='rgb(20, 237, 0)'){
        subject.style.backgroundColor = 'white';
        subject2.style.backgroundColor =' white';
        subject3.style.backgroundColor = 'white';
    }



}