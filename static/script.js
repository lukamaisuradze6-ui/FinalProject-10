let selectedCourseId = null;




let subjects = document.getElementById("subjects");
let popup = document.getElementById("popupp");

popup.style.display = "none";

subjects.onclick = function () {
    if (popup.style.display =='none'){
        popup.style.display = 'flex';
    }else{
        popup.style.display = 'none';
    };
};

let close = document.getElementById("close");

close.onclick = function () {
    popup.style.display = 'none';
};



let subject = document.getElementById("choice");
let subject2 = document.getElementById("choice2");
let subject3 = document.getElementById("choice3");

let fr = document.getElementById("fr");
let yup = document.getElementById("YUP");
let hellno = document.getElementById("HELLNAH");



subject.onclick = function () {
    resetSelection();
    this.style.backgroundColor = 'rgb(20,237,0)';
    selectedCourseId = 1;
};

subject2.onclick = function () {
    resetSelection();
    this.style.backgroundColor = 'rgb(20,237,0)';
    selectedCourseId = 2;
};

subject3.onclick = function () {
    resetSelection();
    this.style.backgroundColor = 'rgb(20,237,0)';
    selectedCourseId = 3;
};

function resetSelection() {
    subject.style.backgroundColor = "white";
    subject2.style.backgroundColor = "white";
    subject3.style.backgroundColor = "white";
}




yup.onclick = function (e) {
    e.preventDefault();

    if (!selectedCourseId) {
        alert("Pick a subject first");
        return;
    }

    window.location.href = "/enroll/" + selectedCourseId;
};






hellno.onclick = function () {
    resetSelection();
    selectedCourseId = null;
};

