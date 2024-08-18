const hostname = window.location.hostname;
function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

// Global variables for wait function
var waiting = false;
var timeRemaining = 0;
var redirectID = 0;
var wait = 0;
var presentEventID = 0;



function readEvent() {
    console.log('readEvent');
    const eventID = document.getElementById('eventNumber').value;

    if (eventID == 0) {
        document.getElementById('eventDescription').innerText = '';
        document.getElementById('hackButton').style.display = 'none';
        document.getElementById('activateButton').style.display = 'none';
        document.getElementById('equipButton').style.display = 'none';
        redirectID = 0;
        hideWait()
        return;
    }

    // Fetch event data from server api
    fetch(`http://${hostname}:8000/event/read/${eventID}`)
    .then(response => response.json())
    .then(json => {
        // Display event data
        console.log(json);
        document.getElementById('eventDescription').innerText = json.description;
        checkForHack(json.hack);
        checkForActivate(json.activate);
        checkOfEquip(json.equip);
        if (json.wait > 0) {
            document.getElementById('eventNumber').readOnly = true;
            timeRemaining = json.wait;
        }
        else {
            timeRemaining = 0;
            document.getElementById('eventNumber').readOnly = false;
        }
        wait = json.wait;
        redirectID = json.redirectID;

    });
}

function checkEventIDChange() {
    const newEventID = document.getElementById('eventNumber').value;
    if (newEventID != presentEventID) {
        presentEventID = newEventID;
        readEvent();
    }
}

function checkForHack(hack) {
    if (hack == 1) {
        document.getElementById('activateButton').style.display = 'block';
    }
    else {
        document.getElementById('activateButton').style.display = 'none';
    }
}

function checkForActivate(activate) {
    if (activate == 1) {
        document.getElementById('activateButton').style.display = 'block';
    }
    else {
        document.getElementById('activateButton').style.display = 'none';
    }
}

function checkOfEquip(equip) {
    if (equip == 1) {
        document.getElementById('equipButton').style.display = 'block';
    }
    else {
        document.getElementById('equipButton').style.display = 'none';
    }
}

function handleWait() {
    if (timeRemaining > 0) {
        document.getElementById('eventNumber').readOnly = true;
        waiting = true;
        document.getElementById('waitMessage').innerText = 'Esperando...';
        timeRemaining--;
        document.getElementById('timeRemaining').innerText = timeRemaining;
    }
    else {
        hideWait();
        if (redirectID > 0 && waiting == true) {
            console.log('Redirecting to event: ' + redirectID);
            document.getElementById('eventNumber').value = redirectID;
            checkEventIDChange()
        }
        document.getElementById('eventNumber').readOnly = false;
        waiting = false;
    }
}

function hideWait() {
    document.getElementById('waitMessage').innerText = '';
    document.getElementById('timeRemaining').innerText = '';
}

function activateEvent() {
    if (waiting == false) {
        console.log('Redirecting to event: ' + redirectID);
        document.getElementById('eventNumber').value = redirectID;
        checkEventIDChange()
    }
}

checkEventIDChange();
setInterval(checkEventIDChange, 100);
setInterval(handleWait, 1000);
document.getElementById("activateButton").addEventListener("click", activateEvent);