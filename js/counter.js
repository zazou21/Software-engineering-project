//quantity counter
const plus = document.querySelector(".plus");
const minus = document.querySelector(".minus");
const number = document.querySelector(".number");
let count = 01;
plus.onclick = function () {
    count++;
    if (count < 10) {
        count = "0" + count;
    };
    number.innerHTML = count;
}
minus.onclick = function () {
    if (count > 1) {
        count--;
        if (count < 10) {
            count = "0" + count;
        };
        number.innerHTML = count;
    }

}
