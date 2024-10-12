document.addEventListener('DOMContentLoaded', function() {
    const wrestlerForm = document.getElementById('wrestler-form');
    const wrestlerStats = document.getElementById('wrestler-stats');

    wrestlerForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const wrestlerName = document.getElementById('wrestler-name').value;
        
        fetch(`http://localhost:8000/wrestlers/name/${wrestlerName}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    wrestlerStats.innerHTML = `<p>Error: ${data.error}</p>`;
                } else {
                    const wrestler = data.wrestler;
                    const championships = data.championships;
                    wrestlerStats.innerHTML = `
                        <img src="${wrestler.image_url}" alt="${wrestler.name}" style="width: 200px; height: auto;">
                        <h2>${wrestler.name}</h2>
                        <p>Finishing Move: ${wrestler.finishing_move}</p>
                        <p>Height: ${wrestler.height_feet}'${wrestler.height_inches}"</p>
                        <p>Weight: ${wrestler.weight_lbs} lbs</p>
                        <p>Championships: ${championships.length > 0 ? championships.join(', ') : 'None'}</p>
                    `;
                }
            })
            .catch(error => {
                wrestlerStats.innerHTML = `<p>Error: Unable to fetch wrestler data</p>`;
                console.error('Error:', error);
            });    });
});