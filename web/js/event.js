const hostname = window.location.hostname;
function returnToLogin() {
    if (sessionStorage.getItem("characterID")==null) {
        window.location.href = 'login.html';
    }
    if (sessionStorage.getItem("apiServer")==null) {
        window.location.href = 'login.html'
    }
}

returnToLogin();

// Global variables for wait function
var waiting = false;
var timeRemaining = 0;
var redirectID = 0;
var hackTarget = 0;
var wait = 0;
var eventID = 0;
var presentEventID = 0;
var characterID = sessionStorage.getItem("characterID");
var hackValue = 0;
var notAutoJump = false;



function readEvent() {
    console.log('readEvent');
    eventID = document.getElementById('eventNumber').value;

    if (eventID == 0) {
        document.getElementById('eventDescription').innerText = '';
        document.getElementById('hackButton').style.display = 'none';
        document.getElementById('activateButton').style.display = 'none';
        document.getElementById('deactivateButton').style.display = 'none';
        redirectID = 0;
        hackTarget = 0;
        hideWait()
        return;
    }

    // Fetch event data from server api
    fetch(`${sessionStorage.getItem("apiServer")}/event/read/${eventID}`)
    .then(response => response.json())
    .then(json => {
        // Display event data
        console.log(json);
        if (json.status == 200)
        {
            document.getElementById('eventDescription').innerText = json.description;
            hackTarget = json.hack;
            checkForHack(json.hack);
            checkForActivate(json.activate);
            checkOfEquip(json.equip);
            if (json.activate || json.equip || json.hack) {
                notAutoJump = true;
            }
            else {
                notAutoJump = false;
            }
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
        }
        else
        {
            document.getElementById('eventDescription').innerText = `ERROR ${json.status}`;
            checkForHack(0);
            checkForActivate(0);
            checkOfEquip(0);
            hackTarget = 0;
            notAutoJump = 0;
        }
        if (json.activated) {
            document.getElementById('eventNumber').value = redirectID;
            checkEventIDChange()
        }
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
    if (hack != 0) {
        document.getElementById('hackButton').style.display = 'block';
    }
    else {
        document.getElementById('hackButton').style.display = 'none';
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
        document.getElementById('deactivateButton').style.display = 'block';
    }
    else {
        document.getElementById('deactivateButton').style.display = 'none';
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
        if (redirectID > 0 && waiting == true && notAutoJump == false) {
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
        fetch(`${sessionStorage.getItem("apiServer")}/event/activate/${eventID}`,{
            method: 'PUT',
        })
        document.getElementById('eventNumber').value = redirectID;
        checkEventIDChange()
    }
}

function deactivateEvent() {
    if (waiting == false) {
        console.log('Deactivating event: ' + redirectID);
        fetch(`${sessionStorage.getItem("apiServer")}/event/deactivate/${redirectID}`,{
            method: 'PUT',
        })
        document.getElementById('eventNumber').value = 0;
        checkEventIDChange()
    }
}0

function hack() {
    if (waiting == false) {
        console.log(`Hacking is ${hackValue}`)
        fetch(`${sessionStorage.getItem("apiServer")}/roll/${hackValue}`)
        .then(response => response.json())
        .then(json => {
            console.log(json);
            if (hackTarget <= json.result) {
                document.getElementById('eventNumber').value = redirectID;
                checkEventIDChange()
            }
            else {
                document.getElementById('eventNumber').value = 0;
                checkEventIDChange()
            }
        });
    }
}

function getHackValue(ID){
    // Fetch character data from server api
    fetch(`${sessionStorage.getItem("apiServer")}/character/${characterID}`)
    .then(response => response.json())
    .then(json => {
        // Display character data
        console.log(json);
        console.log(`Hacking value is ${json.Hacking}`)
        hackValue = json.Hacking;
    });
}

getHackValue(characterID);
document.getElementById('eventNumber').value = 0;
readEvent();
// checkEventIDChange();
// setInterval(checkEventIDChange, 100);
setInterval(handleWait, 1000);
document.getElementById("activateButton").addEventListener("click", activateEvent);
document.getElementById("deactivateButton").addEventListener("click", deactivateEvent);
document.getElementById("hackButton").addEventListener("click", hack);
document.getElementById("readButton").addEventListener("click", checkEventIDChange);