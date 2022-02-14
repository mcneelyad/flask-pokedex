window.addEventListener("DOMContentLoaded", () =>{
    // initialize the favorites list from localStorage
    var favorites = JSON.parse(localStorage.getItem("pokemonList"));
    if (favorites) {
        console.log(favorites);
        favorites.forEach(function(favorite){
            var li = document.createElement("li");
            li.classList.add("pokemon-name");
            li.innerHTML = favorite;
            document.getElementById("favorites").appendChild(li);
        });
    } else { 
        // if there is no list, show message saying no favorites
        document.getElementById("favorites").innerHTML = "No favorites yet!";
    }
});

// get the type of pokemon
var type = document.getElementsByClassName("type");

// for eqch type returned, 
// add a class to the element that will assign the correct color
for (let i = 0; i < type.length; i++) {
    var pokemonItem = type[i].innerHTML.toLowerCase();
    type[i].classList.add(pokemonItem);
}

// initialize the localstorage array to store the pokemon
var pokemon = [];

var addButton = document.getElementById("add");

addButton.addEventListener("click", () => {
    var pokemonName = document.getElementById("pokemonName").innerHTML;
    var pokemonList = JSON.parse(localStorage.getItem("pokemonList"));

    if (pokemonList == null) {
        pokemonList = [];
    }

    if (!pokemonList.includes(pokemonName)) {
        pokemonList.push(pokemonName);
        localStorage.setItem("pokemonList", JSON.stringify(pokemonList));
        alert("Added to your list!");
        window.location.href = "/";
    }
    else {
        alert("Already in your list!");
    }
});