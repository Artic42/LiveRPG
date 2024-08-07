function sendCharacterChange() { 
    // Get form values
    const name = document.getElementById('name').value;
    const health = document.getElementById('health').value;
    const strength = document.getElementById('strength').value;
    const hacking = document.getElementById('hacking').value;
    const medicine = document.getElementById('medicine').value;
    const background = document.getElementById('background').value;

    // Create a JSON object with the form values
    const characterData = {
        name: name,
        health: health,
        strength: strength,
        hacking: hacking,
        medicine: medicine,
        background: background
    };

    // Log the JSON object to the console
    console.log(JSON.stringify(characterData, null, 2));
}

function readCharacter() {
    // Get values from database
    // Put values in the form
}


// Add event listener to the buttons
document.getElementById("buttonSave").addEventListener("click", sendCharacterChange);
document.getElementById("buttonLoad").addEventListener("click", readCharacter);