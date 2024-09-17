function returnToLogin() {
    if (sessionStorage.getItem("characterID")==null) {
        window.location.href = 'login.html';
    }
    if (sessionStorage.getItem("apiServer")==null) {
        window.location.href = 'login.html'
    }
}

function logout() {
    sessionStorage.removeItem('characterID');
    returnToLogin();
}

function handleControlPanelAccess() {
    const characterID = sessionStorage.getItem('characterID');
    if (characterID != -1) {
        document.getElementById('buttonControlPanel').style.display = 'none';
    }
    else {
        document.getElementById('buttonControlPanel').style.display = 'block';
    }
}

returnToLogin();
handleControlPanelAccess();
document.getElementById('buttonLogout').addEventListener('click', logout);