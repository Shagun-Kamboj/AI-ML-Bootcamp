=============================
// Live Clock
// =============================

function updateClock() {

    const clock = document.getElementById("clock");

    if (!clock) return;

    const now = new Date();

    let hours = now.getHours();
    let minutes = now.getMinutes();
    let seconds = now.getSeconds();

    hours = String(hours).padStart(2, "0");
    minutes = String(minutes).padStart(2, "0");
    seconds = String(seconds).padStart(2, "0");

    clock.innerHTML = ${hours}:${minutes}:${seconds};
}

setInterval(updateClock, 1000);
updateClock();


// =============================
// Greeting
// =============================

function updateGreeting() {

    const greeting = document.getElementById("greeting");

    if (!greeting) return;

    const hour = new Date().getHours();

    let text = "Good Evening";

    if(hour < 12){

        text = "Good Morning";

    }

    else if(hour < 17){

        text = "Good Afternoon";

    }

    else{

        text = "Good Evening";

    }

    greeting.innerHTML =
    greeting.innerHTML.replace(
        /Good Morning|Good Afternoon|Good Evening/,
        text
    );

}

updateGreeting();


// =============================
// Card Animation
// =============================

const cards = document.querySelectorAll(".card");

cards.forEach(card=>{

    card.addEventListener("mouseenter",()=>{

        card.style.transform="translateY(-10px) scale(1.03)";

    });

    card.addEventListener("mouseleave",()=>{

        card.style.transform="translateY(0px)";

    });

});


// =============================
// Search Box (UI only)
// =============================

const search = document.querySelector(".action-bar input");

if(search){

search.addEventListener("keyup",function(){

console.log("Searching :",this.value);

});

}