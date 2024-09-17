const hostname = window.location.hostname;
playerID = localStorage.getItem("characterID");
function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();

function readBackground() {
    fetch(`http://lsbapi.artic42.com/character/${playerID}/background`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('background').innerText = json.background;
    });
}

readBackground();