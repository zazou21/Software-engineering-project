//make the size chart button toggle the size chart image

const showsizechartbtn = document.querySelector(".showsizechart");
const sizechartimg = document.querySelector(".sizechart");
sizechartimg.style.display = "none";
showsizechartbtn.onclick = toggleImg;

function toggleImg() {
    if (sizechartimg.style.display == "none") {
        sizechartimg.style.display = "block";
        showsizechartbtn.innerText = "hide size chart";
    } else {
        sizechartimg.style.display = "none";
        showsizechartbtn.innerText = "check size chart";
    }
}

//make the smallimg replace the bigimg when clicked
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


