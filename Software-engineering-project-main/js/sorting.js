document.getElementById("select").addEventListener("change", sortcards);
var originalCards = document.querySelectorAll(".card");//org cards before changing the order

function sortcards() {
    var option = document.getElementById("select").value;//get the value of the selected option

    if (option == "Low to high") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);//array of array-like object(cards)

        //this function returns a -ve num if a < b, 0 if a = b, and a +ve num if a > b
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

function diplaysortedcards(sortedCards) {
    var container = document.querySelector(".container");
    var sortedContainer = document.createElement("div");//creating a new div for the sorted cards
    sortedContainer.className = "row gy-3";//adding bootstrap classes

    for (var i = 0; i < sortedCards.length; i++) {
        var col = document.createElement("div");//creating a new div for each card
        col.className = "col-12 col-md-6 col-lg-4 col-xl-3";//adding bootstrap classes
        col.appendChild(sortedCards[i]);//adding card to the div
        sortedContainer.appendChild(col);//adding the div to the container
    }

    container.innerHTML = "";//removing the original cards
    container.appendChild(sortedContainer);//adding the sorted cards
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


