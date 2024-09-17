const hostname = window.location.hostname;

function returnToLogin() {
    if (sessionStorage.getItem("characterID")!=-1) {
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

    fetch(`${sessionStorage.getItem("apiServer")}/character/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteCharacter() {
    const ID =  document.getElementById('ID').value;

    fetch(`${sessionStorage.getItem("apiServer")}/character/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function createEvent() {
    const ID =  document.getElementById('ID').value;

    fetch(`${sessionStorage.getItem("apiServer")}/event/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteEvent() {
    const ID =  document.getElementById('ID').value;

    fetch(`${sessionStorage.getItem("apiServer")}/event/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function createInformation() {
    const ID =  document.getElementById('ID').value;

    fetch(`${sessionStorage.getItem("apiServer")}/information/create/${ID}`, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}

function deleteInformation() {
    const ID =  document.getElementById('ID').value;

    fetch(`${sessionStorage.getItem("apiServer")}/information/delete/${ID}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(json => console.log(json))
}


document.getElementById("buttonCreate").addEventListener("click", handleCreateButton);
document.getElementById("buttonDelete").addEventListener("click", handleDeleteButton);