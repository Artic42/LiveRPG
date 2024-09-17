const hostname = window.location.hostname;
var showModifyHealth = false;

function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

function readCharacter() {
    const characterID = localStorage.getItem("characterID");

    // Fetch character data from server api
    fetch(`http://lsbapi.artic42.com/character/${characterID}`)
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

function rollStrength() {
    strength = document.getElementById('strengthValue').innerText;

    fetch(`http://lsbapi.artic42.com/roll/${strength}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('rollResult').innerText = "Resultado fuerza " + json.result;
    });
}

function rollHack() {
    hack = document.getElementById('hackValue').innerText;

    fetch(`http://lsbapi.artic42.com/roll/${hack}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('rollResult').innerText = "Resultado hack " + json.result;
    });
}

function rollMedicine() {
    medicine = document.getElementById('medicineValue').innerText;

    fetch(`http://lsbapi.artic42.com/roll/${medicine}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('rollResult').innerText = "Resultado medicina " + json.result;
    });
}

function handleModifyHealth() {
    if (showModifyHealth == true) {
        document.getElementById('modifyHealth').style.display = '';
    } else {
        document.getElementById('modifyHealth').style.display = 'none';
    }
}

function healthButton() {
    if (showModifyHealth == true) {
        showModifyHealth = false;
    }
    else {
        showModifyHealth = true;
    }
    console.log(showModifyHealth);
    handleModifyHealth();
}

function addHealth() {
    health = document.getElementById('healthValue').innerText;
    health = parseInt(health) + 1;
    const characterID = localStorage.getItem("characterID");

    const healthData = {
        health: health
    };

    fetch(`http://lsbapi.artic42.com/character/editHealth/${characterID}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(healthData),
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
        readCharacter();
    });
}

function decreaseHealth() {
    health = document.getElementById('healthValue').innerText;
    health = parseInt(health) - 1;
    const characterID = localStorage.getItem("characterID");

    const healthData = {
        health: health
    };

    fetch(`http://lsbapi.artic42.com/character/editHealth/${characterID}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(healthData),
    })
    .then(response => response.json())
    .then(json => {
        console.log(json);
        readCharacter();
    });
}

// Run readCharacter immediately
readCharacter();
handleModifyHealth();

// Set interval to run readCharacter every 30 seconds (30000 milliseconds)
setInterval(readCharacter, 30000);
document.getElementById('strengthButton').addEventListener('click', rollStrength);
document.getElementById('hackButton').addEventListener('click', rollHack);
document.getElementById('medicineButton').addEventListener('click', rollMedicine);
document.getElementById('healthButton').addEventListener('click', healthButton);
document.getElementById('increaseHealthButton').addEventListener('click', addHealth);
document.getElementById('decreaseHealthButton').addEventListener('click', decreaseHealth);