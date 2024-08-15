const hostname = window.location.hostname;
var characterID = 0;

function sendEventChange() { 
    // Get form values
    const description = document.getElementById('description').value;
    const activate = document.getElementById('activate').value;
    const hack = document.getElementById('hack').value;
    const equip = document.getElementById('equip').value;
    const wait = document.getElementById('wait').value;
    const activated = document.getElementById('activated').value;

    // Create a JSON object with the form values
    const eventData = {
        description: description,
        activate: activate,
        hack: hack,
        equip: equip,
        wait: wait,
        activated: activated
    };
}


