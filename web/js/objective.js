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

playerID = sessionStorage.getItem("characterID");

function readMainObjective() {
    fetch(`${sessionStorage.getItem("apiServer")}/character/${playerID}/mainObjective`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('mainObjectiveText').innerText = json.mainObjective;
    });
}

function readSecondaryObjective() {
    fetch(`${sessionStorage.getItem("apiServer")}/character/${playerID}/secondaryObjective`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('secondaryObjectivesText').innerText = json.secondaryObjective;
    });
}

function readDefeatCondition() {
    fetch(`${sessionStorage.getItem("apiServer")}/character/${playerID}/loseCondition`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('defeatConditionsText').innerText = json.loseCondition;
    });
}

readDefeatCondition();
readMainObjective();
readSecondaryObjective();