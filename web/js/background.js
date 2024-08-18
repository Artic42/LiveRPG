const hostname = window.location.hostname;
playerID = localStorage.getItem("characterID");
function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

function readBackground() {
    fetch(`http://${hostname}:8000/character/${playerID}/background`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('background').innerText = json.background;
    });
}

readBackground();