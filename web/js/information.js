const hostname = window.location.hostname;
const playerID = 1;

// Global variables for wait function
var presentID = 0;


async function getOptions() {
    const selectElement = document.getElementById('informationDropdown');
    const response = await fetch(`http://${hostname}:8000/information/readKnownCharacters/${playerID}`);
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
    const response = await fetch(`http://${hostname}:8000/information/readAboutName/${ID}`);
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
    fetch(`http://${hostname}:8000/information/readDescription/${presentID}`)
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