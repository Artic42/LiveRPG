const hostname = window.location.hostname;
var eventID = 0;

function returnToLogin() {
    if (sessionStorage.getItem("characterID")!=-1) {
    window.location.href = 'login.html';
}}

returnToLogin();

function sendEventChange() { 
    // Get form values
    const description = document.getElementById('descriptionTextInput').value;
    const activate = readCheckbox('activate');
    const hack = readCheckbox('hack');
    const equip = readCheckbox('equip');
    const wait = document.getElementById('wait').value;
    const activated = readCheckbox('activated');
    const redirectID = document.getElementById('redirectID').value;

    // Create a JSON object with the form values
    const eventData = {
        description: description,
        activate: activate,
        hack: hack,
        equip: equip,
        wait: wait,
        activated: activated,
        redirectID: redirectID
    };

    console.log(eventData);

    fetch(`${sessionStorage.getItem("apiServer")}/event/editEvent/${eventID}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(eventData),
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function readEvent() {
    eventID = document.getElementById('eventID').value;
    document.getElementById('EventIDNumber').innerText = "ID: " + eventID;

    fetch(`${sessionStorage.getItem("apiServer")}/event/read/${eventID}`)
    .then(response => response.json())
    .then(json => {
        // Display event data
        console.log(json);
        document.getElementById('descriptionTextInput').value = json.description;
        handleCheckbox('activate', json.activate);
        handleCheckbox('hack', json.hack);
        handleCheckbox('equip', json.equip);
        document.getElementById('wait').value = json.wait;
        handleCheckbox('activated', json.activated);
        document.getElementById('redirectID').value = json.redirectID;
    });
}

function activateCheckbox(id) {
    const checkbox = document.getElementById(id);
    checkbox.checked = true;
}

function deactivateCheckbox(id) {
    const checkbox = document.getElementById(id);
    checkbox.checked = false;
}

function handleCheckbox(id, value) {
    if (value == 1) {
        activateCheckbox(id);
    } else {
        deactivateCheckbox(id);
    }
}

function readCheckbox(id) {
    const checkbox = document.getElementById(id);
    return checkbox.checked ? 1 : 0;
}
// Add event listener to the buttons
document.getElementById("buttonSave").addEventListener("click", sendEventChange);
document.getElementById("buttonLoad").addEventListener("click", readEvent);
