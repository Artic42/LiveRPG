const hostname = window.location.hostname;
var informationID = 0;

function returnToLogin() {
    if (localStorage.getItem("characterID")!=-1) {
    window.location.href = 'login.html';
}}

returnToLogin();

function sendInformationChange() {
    // Get form values
    const known = document.getElementById('knownID').value;
    const about = document.getElementById('aboutID').value;
    const description = document.getElementById('descriptionTextInput').value;

    // Create a JSON object with the form values
    const informationData = {
        knownCharacter: known,
        aboutCharacter: about,
        description: description
    };

    console.log(informationData);

    fetch(`http://lsbapi.artic42.com/information/editFull/${informationID}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(informationData),
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function readInformation() {
    informationID = document.getElementById('informationID').value;
    document.getElementById('InformationIDNumber').innerText = "ID: " + informationID;

    fetch(`http://lsbapi.artic42.com/information/readFull/${informationID}`)
    .then(response => response.json())
    .then(json => {
        // Display information data
        console.log(json);
        document.getElementById('knownID').value = json.knownCharacter;
        document.getElementById('aboutID').value = json.aboutCharacter;
        document.getElementById('descriptionTextInput').value = json.description;
    });
}


// Add event listener to the buttons
document.getElementById("buttonSave").addEventListener("click", sendInformationChange);
document.getElementById("buttonLoad").addEventListener("click", readInformation);