const hostname = window.location.hostname;
function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

function readCharacter() {
    const characterID = localStorage.getItem("characterID");

    // Fetch character data from server api
    fetch(`http://${hostname}:8000/character/${characterID}`)
    .then(response => response.json())
    .then(json => {
        // Display character data
        console.log(json);
        console.log(json.Name);
        document.getElementById('name').innerText = json.Name;
        document.getElementById('healthValue').innerText = json.Health;
        document.getElementById('strengthValue').innerText = json.Strength;
        document.getElementById('hackValue').innerText = json.Hacking;
        document.getElementById('medicineValue').innerText = json.Medicine;
    });
}

function rollMedicine() {
    console.log("Rolling Medicine");
    rollDice(document.getElementById('medicineValue').innerText);
}

function rollStrength() {
    console.log("Rolling Strength");
    rollDice(document.getElementById('strengthValue').innerText);
}

function rollHack() {
    console.log("Rolling Hack");
    rollDice(document.getElementById('hackValue').innerText);
}


function rollDice(dices) {
    // Fetch character data from server api
    fetch(`http://${hostname}:8000/roll/${dices}`)
    .then(response => response.json())
    .then(json => {
        // Display character data
        console.log(json);
    });
}


// Run readCharacter immediately
readCharacter();

// Set interval to run readCharacter every 30 seconds (30000 milliseconds)
setInterval(readCharacter, 30000);