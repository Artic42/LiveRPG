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

document.getElementById('buttonDownload').addEventListener('click', downloadDatabase);