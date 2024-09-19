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
var presentID = 0;


async function getOptions() {
    const characterID = sessionStorage.getItem("characterID");
    const selectElement = document.getElementById('informationDropdown');
    const response = await fetch(`${sessionStorage.getItem("apiServer")}/information/readKnownCharacters/${characterID}`);
    const json = await response.json();
    console.log(json);
    const IDs = json.knownIDs;
    console.log(IDs);
    for (const ID of IDs) {
        console.log(ID);
        const name = await getNameAbout(ID);
        console.log(name);
        const newOption = document.createElement('option');
        newOption.value = ID;
        newOption.innerText = name; 
        selectElement.appendChild(newOption);           
    }
}

async function getNameAbout(ID) {
    const response = await fetch(`${sessionStorage.getItem("apiServer")}/information/readAboutName/${ID}`);
    const json = await response.json();
    console.log(json);
    console.log(json.name);
    return json.name;
}

function readDescription() {
    const descriptionElement = document.getElementById('description');
    if (presentID == 0) {
        descriptionElement.innerText = '';
        return;
    }
    fetch(`${sessionStorage.getItem("apiServer")}/information/readDescription/${presentID}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        descriptionElement.innerText = json.description;
    });
}

function cleanSelect() {
    const selectElement = document.getElementById('informationDropdown');
    selectElement.innerHTML = '';
}

function checkCharacterChange() {
    const newID = document.getElementById('informationDropdown').value;
    if (newID != presentID) {
        presentID = newID;
        readDescription();
    }
}

// Call the function to populate the select element
readDescription();
getOptions();
setInterval(checkCharacterChange, 1000);