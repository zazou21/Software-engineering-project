//the idea is to add all the cards to an array then sort the array
//we delete the original cards from the container and add the sorted cards to the container
//the original cards are stored in variable in case we want to display them again(default)

document.getElementById("select").addEventListener("change", sortcards);
var originalCards = document.querySelectorAll(".card");

function sortcards() {
    var option = document.getElementById("select").value;

    if (option == "Low to high") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);


        sortedCards.sort(function (a, b) {
            return parseInt(a.querySelector(".price").textContent) - parseInt(b.querySelector(".price").textContent);//text content of the price
        });

        diplaysortedcards(sortedCards);
    }
    else if (option == "High to low") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);
        sortedCards.sort(function (a, b) {
            return parseInt(b.querySelector(".price").textContent) - parseInt(a.querySelector(".price").textContent);
        });
        diplaysortedcards(sortedCards);
    }
    else if (option == "Default") {
        displayoriginalcards();
    }
}
//making sure that the added cards have the same format as the original cards when added
function diplaysortedcards(sortedCards) {
    var container = document.querySelector(".container");
    var sortedContainer = document.createElement("div");
    sortedContainer.className = "row gy-3";

    for (var i = 0; i < sortedCards.length; i++) {
        var col = document.createElement("div");
        col.className = "col-12 col-md-6 col-lg-4 col-xl-3";
        col.appendChild(sortedCards[i]);
        sortedContainer.appendChild(col);
    }

    container.innerHTML = "";
    container.appendChild(sortedContainer);
}

function displayoriginalcards() {
    var container = document.querySelector(".container");
    var originalContainer = document.createElement("div");
    originalContainer.className = "row original-cards";

    for (var i = 0; i < originalCards.length; i++) {
        var col = document.createElement("div");
        col.className = "col-lg-3 col-md-4 col-sm-6 mb-4";
        col.appendChild(originalCards[i].cloneNode(true));
        originalContainer.appendChild(col);
    }

    container.innerHTML = "";
    container.appendChild(originalContainer);
}


