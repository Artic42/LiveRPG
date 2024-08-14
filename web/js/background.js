const hostname = window.location.hostname;
const playerID = 1;

function readBackground() {
    fetch(`http://${hostname}:8000/character/${playerID}/background`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('background').innerText = json.background;
    });
}

readBackground();