const hostname = window.location.hostname;

function downloadDatabase() {
    fetch(`http://${hostname}:8000/downloadDatabase`, {
        method: 'GET',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.blob();
    })
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'Database.db';
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error('Download failed:', error));
}

function uploadDatabase() {
    const file = document.getElementById('path').files[0];
    if (!file) {
        alert('Please select a file to upload');
        return;
    }

    console.log(file);

    const formData = new FormData();
    formData.append('file', file);

    fetch(`http://${hostname}:8000/uploadDatabase`, {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
}

document.getElementById('buttonDownload').addEventListener('click', downloadDatabase);
document.getElementById('buttonUpload').addEventListener('click', uploadDatabase);