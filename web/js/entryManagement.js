const hostname = window.location.hostname;

function returnToLogin() {
    if (localStorage.getItem("characterID")!=-1) {
    window.location.href = 'login.html';
}}

returnToLogin();

function handleCreateButton() {
    const selector = document.getElementById('selectorDropdown').value;

    switch (selector) {
        case 'character':
            createCharacter();
            break;
        case 'event':
            createEvent();
            break;
        case 'information':
            createInformation();
            break;
        default:
            console.log('Invalid selector');
    }
}

function handleDeleteButton() {
    const selector = document.getElementById('selectorDropdown').value;

    switch (selector) {
        case 'character':
            deleteCharacter();
            break;
        case 'event':
            deleteEvent();
            break;
        case 'information':
            deleteInformation();
            break;
        default:
            console.log('Invalid selector');
    }
}


function createCharacter() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://lsbapi.artic42.com/character/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteCharacter() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://lsbapi.artic42.com/character/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function createEvent() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://lsbapi.artic42.com/event/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteEvent() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://lsbapi.artic42.com/event/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function createInformation() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://lsbapi.artic42.com/information/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteInformation() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://lsbapi.artic42.com/information/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}


document.getElementById("buttonCreate").addEventListener("click", handleCreateButton);
document.getElementById("buttonDelete").addEventListener("click", handleDeleteButton);