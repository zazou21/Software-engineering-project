//make the smallimg replace the bigimg when clicked
//the user can achieve this by clicking on the smallimg or the radiobtn

//1 using btns selection
var smallimgs = document.querySelectorAll(".smallimg");
var bigimg = document.querySelector(".bigimg");
var radiobtn = document.querySelectorAll(".radiobtn");
for (let j = 0; j < radiobtn.length; j++) {
    radiobtn[j].onclick = function () {
        bigimg.src = smallimgs[j].src;
    }
}

//2 using img selection
for (let i = 0; i < smallimgs.length; i++) {

    smallimgs[i].onclick = function () {
        bigimg.src = smallimgs[i].src;
        radiobtn[i].checked = true;
    }
}


