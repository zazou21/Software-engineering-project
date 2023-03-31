

const carts = document.querySelectorAll(".add-to-cart");
carts.forEach(cart => {
    cart.addEventListener('click', (event) => {
        event.preventDefault();
    });
});






const hearts = document.querySelectorAll(".heart");
hearts.forEach(heart => {
    heart.addEventListener('click', (event) => {
        event.preventDefault();
    });
});

const deletes = document.querySelectorAll(".delete");
deletes.forEach(icon => {
    icon.addEventListener('click', (event) => {
        event.preventDefault();
    });
});





