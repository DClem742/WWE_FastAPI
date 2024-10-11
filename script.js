document.addEventListener('DOMContentLoaded', function() {
    const wrestlerForm = document.getElementById('wrestler-form');
    const wrestlerStats = document.getElementById('wrestler-stats');

    wrestlerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const wrestlerName = document.getElementById('wrestler-name').value;
        
        fetch(`http://localhost:8000`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    wrestlerStats.innerHTML = `<p>Error: ${data.error}</p>`;
                } else {
                    wrestlerStats.innerHTML = `
                        <h2>${data.name}</h2>
                        <p>Finishing Move: ${data.finishing_move}</p>
                        <p>Height: ${data.height_feet}'${data.height_inches}"</p>
                        <p>Weight: ${data.weight_lbs} lbs</p>
                    `;
                }
            })
            .catch(error => {
                wrestlerStats.innerHTML = `<p>Error: Unable to fetch wrestler data</p>`;
                console.error('Error:', error);
            });
    });
});
