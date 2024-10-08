const hostname = window.location.hostname;
var showModifyHealth = false;

function returnToLogin() {
    if (sessionStorage.getItem("characterID")==null) {
        window.location.href = 'login.html';
    }
    if (sessionStorage.getItem("apiServer")==null) {
        window.location.href = 'login.html'
    }
}

returnToLogin();

function readCharacter() {
    const characterID = sessionStorage.getItem("characterID");

    // Fetch character data from server api
    fetch(`${sessionStorage.getItem("apiServer")}/character/${characterID}`)
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
    const strength = document.getElementById('strengthValue').innerText;

    fetch(`${sessionStorage.getItem("apiServer")}/roll/${strength}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('rollResult').innerText = "Resultado combate " + json.result;
    });
}

function rollHack() {
    const hack = document.getElementById('hackValue').innerText;

    fetch(`${sessionStorage.getItem("apiServer")}/roll/${hack}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('rollResult').innerText = "Resultado hack " + json.result;
    });
}

function rollMedicine() {
    const medicine = document.getElementById('medicineValue').innerText;

    fetch(`${sessionStorage.getItem("apiServer")}/roll/${medicine}`)
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
    const characterID = sessionStorage.getItem("characterID");

    const healthData = {
        health: health
    };

    fetch(`${sessionStorage.getItem("apiServer")}/character/editHealth/${characterID}`, {
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
    const characterID = sessionStorage.getItem("characterID");

    const healthData = {
        health: health
    };

    fetch(`${sessionStorage.getItem("apiServer")}/character/editHealth/${characterID}`, {
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