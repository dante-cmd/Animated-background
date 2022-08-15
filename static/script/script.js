var ws = new WebSocket("ws://localhost:8000/ws");


// let cards = document.getElementById("cards-main");
ws.addEventListener("message", function(e) {
    let cards= document.getElementById("main");
    // cards.style.backgroundColor = "red";
    let colors = e.data.split(',')
    cards.style.background = "linear-gradient(to bottom," + colors[0] + "0%," + colors[1]+ "  100%)";

    // console.log("linear-gradient(to bottom," + colors[0] + "0%," + colors[1]+ "  100%)")

} );

let cards = document.getElementById("cards-main");
cards.addEventListener("mouseover", function(e) {
    
    if (e.target.classList.contains("src")) {
        // console.log(e.target.getAttribute("src"));
        ws.send(e.target.getAttribute("src"));
        // console.log(e.target.classList.value);
        // e.target.getAttribute("src").value
        // console.log(e.target.getAttribute("src"));
    };
} );

// card_1.background = "linear-gradient(to bottom, #000000 0%, #ffffff 100%)";
// console.log(card_1);