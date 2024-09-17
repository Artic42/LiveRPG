const hostname = window.location.hostname;

function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const userData = {
        username: username,
        password: password};

    console.log(userData);

    fetch(`http://lsbapi.artic42.com/login`, {
        method: 'POST',
        body: JSON.stringify(userData),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(json => {
        if (json.characterID != null) {
            sessionStorage.setItem('characterID', json.characterID);
            window.location.href = 'index.html';
        } else {
            alert('Login failed');
        }
    });
}

document.getElementById('loginButton').addEventListener('click', login);