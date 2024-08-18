function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

function logout() {
    localStorage.removeItem('characterID');
    returnToLogin();
}

function handleControlPanelAccess() {
    const characterID = localStorage.getItem('characterID');
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