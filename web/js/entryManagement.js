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

    fetch(`http://${hostname}:8000/character/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteCharacter() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://${hostname}:8000/character/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function createEvent() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://${hostname}:8000/event/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteEvent() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://${hostname}:8000/event/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function createInformation() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://${hostname}:8000/information/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteInformation() {
    const ID =  document.getElementById('ID').value;

    fetch(`http://${hostname}:8000/information/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}


document.getElementById("buttonCreate").addEventListener("click", handleCreateButton);
document.getElementById("buttonDelete").addEventListener("click", handleDeleteButton);