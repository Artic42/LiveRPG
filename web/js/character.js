const hostname = window.location.hostname;
const playerID = 1;

function readCharacter() {
    const characterID = 1;

    // Fetch character data from server api
    fetch(`http://${hostname}:8000/character/${playerID}`)
    .then(response => response.json())
    .then(json => {
        // Display character data
        console.log(json);
        console.log(json.Name);
        document.getElementById('name').innerText = json.Name;
        document.getElementById('healthValue').innerText = json.Health;
        document.getElementById('strengthValue').innerText = json.Strength;
        document.getElementById('hackValue').innerText = json.Hacking;
        document.getElementById('medicineValue').innerText = json.Medicine;
    });
}
   

// Run readCharacter immediately
readCharacter();

// Set interval to run readCharacter every 30 seconds (30000 milliseconds)
setInterval(readCharacter, 30000);