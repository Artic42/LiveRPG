function returnToLogin() {
    if (localStorage.getItem("characterID")==null) {
    window.location.href = 'login.html';
}}

returnToLogin();