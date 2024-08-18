const hostname = window.location.hostname;
function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

playerID = localStorage.getItem("characterID");

function readMainObjective() {
    fetch(`http://${hostname}:8000/character/${playerID}/mainObjective`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('mainObjectiveText').innerText = json.mainObjective;
    });
}

function readSecondaryObjective() {
    fetch(`http://${hostname}:8000/character/${playerID}/secondaryObjective`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('secondaryObjectivesText').innerText = json.secondaryObjective;
    });
}

function readDefeatCondition() {
    fetch(`http://${hostname}:8000/character/${playerID}/loseCondition`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('defeatConditionsText').innerText = json.loseCondition;
    });
}

readDefeatCondition();
readMainObjective();
readSecondaryObjective();