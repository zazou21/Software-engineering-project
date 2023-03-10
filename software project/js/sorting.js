document.getElementById("select").addEventListener("change", sortCards);
var originalCards = document.querySelectorAll(".card");

function sortCards() {
    var option = document.getElementById("select").value;

    if (option == "Low to high") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);
        sortedCards.sort(function (a, b) {
            return parseInt(a.querySelector(".price").textContent.slice(1)) - parseInt(b.querySelector(".price").textContent.slice(1));
        });
        renderSortedCards(sortedCards);
    } else if (option == "High to low") {
        var cards = document.querySelectorAll(".card");
        var sortedCards = Array.from(cards);
        sortedCards.sort(function (a, b) {
            return parseInt(b.querySelector(".price").textContent.slice(1)) - parseInt(a.querySelector(".price").textContent.slice(1));
        });
        renderSortedCards(sortedCards);
    } else if (option == "Default") {
        renderOriginalCards();
    }
}

function renderSortedCards(sortedCards) {
    var container = document.querySelector(".container");
    var sortedContainer = document.createElement("div");
    sortedContainer.className = "row sorted-cards";

    for (var i = 0; i < sortedCards.length; i++) {
        var col = document.createElement("div");
        col.className = "col-lg-3 col-md-4 col-sm-6 mb-4";
        col.appendChild(sortedCards[i]);
        sortedContainer.appendChild(col);
    }

    container.innerHTML = "";
    container.appendChild(sortedContainer);
}

function renderOriginalCards() {
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


