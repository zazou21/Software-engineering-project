const deleteButtons = document.querySelectorAll(".delete");

deleteButtons.forEach((button) => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        const card = button.closest(".card");
        const column = card.parentNode;
        const row = column.parentNode;
        row.removeChild(column);
    });
});

