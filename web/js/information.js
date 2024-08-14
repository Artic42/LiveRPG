const hostname = window.location.hostname;
const playerID = 1;

// Global variables for wait function

function getOptions() {
    fetch(`http://${hostname}:8000/information/readKnownCharacters/${playerID}`) 
    .then(response => response.json())
    .then(json => {
        console.log(json);
        const IDs = json.KnownIDs;

        for (const ID in IDs) {
            
        }
    });
}

function getNameAbout(ID) {
    fetch(`http://${hostname}:8000/information/readAboutName/${ID}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
    });
}