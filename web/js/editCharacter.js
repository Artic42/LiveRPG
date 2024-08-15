const hostname = window.location.hostname;
var characterID = 0;

function sendCharacterChange() { 
    // Get form values
    const name = document.getElementById('name').value;
    const player = document.getElementById('player').value;
    const health = document.getElementById('health').value;
    const strength = document.getElementById('strength').value;
    const hacking = document.getElementById('hacking').value;
    const medicine = document.getElementById('medicine').value;
    const background = document.getElementById('backgroundTextInput').value;
    const mainObjective = document.getElementById('mainObjectiveTextInput').value;
    const secondaryObjective = document.getElementById('secondaryObjectiveTextInput').value;
    const loseCondition = document.getElementById('loseConditionTextInput').value;

    // Create a JSON object with the form values
    const characterData = {
        name: name,
        player: player,
        health: health,
        strength: strength,
        hacking: hacking,
        medicine: medicine,
        background: background,
        mainObjective: mainObjective,
        secondaryObjective: secondaryObjective,
        loseCondition: loseCondition
    };

    // Log the JSON object to the console
    console.log(characterData);

    fetch(`http://${hostname}:8000/character/edit/1`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(characterData),
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function readCharacter() {
    characterID = document.getElementById('characterID').value;
    if (characterID == 0 || characterID == null || characterID == undefined) {
        alert("Please enter a valid character ID");
        return;
    }
    document.getElementById('characterIDText').innerText = `Character ID: ${characterID}`;
    fetch(`http://${hostname}:8000/character/${characterID}`)
    .then(response => response.json())
    .then(json => {
        console.log(json);
        document.getElementById('name').value = json.Name;
        document.getElementById('player').value = json.Player;
        document.getElementById('health').value = Number(json.Health);
        document.getElementById('strength').value = Number(json.Strength);
        document.getElementById('hacking').value = Number(json.Hacking);
        document.getElementById('medicine').value = Number(json.Medicine);
        document.getElementById('backgroundTextInput').value = json.Background;
        document.getElementById('mainObjectiveTextInput').value = json.MainObjective;
        document.getElementById('secondaryObjectiveTextInput').value = json.SecondaryObjective;
        document.getElementById('loseConditionTextInput').value = json.LoseCondition;
    })
}


// Add event listener to the buttons
document.getElementById("buttonSave").addEventListener("click", sendCharacterChange);
document.getElementById("buttonLoad").addEventListener("click", readCharacter);