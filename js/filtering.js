document.getElementById("select2").addEventListener("change", filtercards);
var orgcards = document.querySelectorAll(".card");


function filtercards() {
    var option2 = document.getElementById("select2").value;

    if (option2 == "Male") {
        var cardsM = orgcards
        var filteredCardsM = Array.from(cardsM);
        for (let i = 0; i < filteredCardsM.length; i++) {
            if (filteredCardsM[i].classList.contains("female")) {
                filteredCardsM.splice(i, 1);
                i--;
            }
        }

        diplayfilteredcards(filteredCardsM);
    }
    else if (option2 == "Female") {
        var cardsF = orgcards
        var filteredCardsF = Array.from(cardsF);
        for (let i = 0; i < filteredCardsF.length; i++) {
            if (filteredCardsF[i].classList.contains("male")) {
                filteredCardsF.splice(i, 1);
                i--;
            }
        }

        diplayfilteredcards(filteredCardsF);
    }
    else if (option2 == "Default") {
        displayoriginalcards();
    }


    function diplayfilteredcards(filteredcards) {
        var container = document.querySelector(".container");
        var filteredcontainer = document.createElement("div");
        filteredcontainer.className = "row gy-3";

        for (var i = 0; i < filteredcards.length; i++) {
            var col = document.createElement("div");
            col.className = "col-12 col-md-6 col-lg-4 col-xl-3";
            col.appendChild(filteredcards[i]);
            filteredcontainer.appendChild(col);
        }

        container.innerHTML = "";
        container.appendChild(filteredcontainer);
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
}








