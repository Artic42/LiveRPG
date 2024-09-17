const hostname = window.location.hostname;
function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

playerID = localStorage.getItem("characterID");

function readMainObjective() {
    fetch(`http://lsbapi.artic42.com/character/${playerID}/mainObjective`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('mainObjectiveText').innerText = json.mainObjective;
    });
}

function readSecondaryObjective() {
    fetch(`http://lsbapi.artic42.com/character/${playerID}/secondaryObjective`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('secondaryObjectivesText').innerText = json.secondaryObjective;
    });
}

function readDefeatCondition() {
    fetch(`http://lsbapi.artic42.com/character/${playerID}/loseCondition`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('defeatConditionsText').innerText = json.loseCondition;
    });
}

readDefeatCondition();
readMainObjective();
readSecondaryObjective();