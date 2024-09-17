const hostname = window.location.hostname;
playerID = sessionStorage.getItem("characterID");
function returnToLogin() {
    if (sessionStorage.getItem("characterID")==null) {
        window.location.href = 'login.html';
    }
    if (sessionStorage.getItem("apiServer")==null) {
        window.location.href = 'login.html'
    }
}

returnToLogin();

function readBackground() {
    fetch(`${sessionStorage.getItem("apiServer")}/character/${playerID}/background`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('background').innerText = json.background;
    });
}

readBackground();