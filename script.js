document.addEventListener('DOMContentLoaded', function() {
    // Get references to important DOM elements
    const wrestlerForm = document.getElementById('wrestler-form');
    const wrestlerStats = document.getElementById('wrestler-stats');

    // Add submit event listener to the wrestler form
    wrestlerForm.addEventListener('submit', function(e) {
        // Prevent the default form submission behavior
        e.preventDefault();
        
        // Get the wrestler name from the input field
        const wrestlerName = document.getElementById('wrestler-name').value;
        
        // Fetch wrestler data from the API
        fetch(`http://localhost:8000/wrestlers/name/${wrestlerName}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    // Display error message if wrestler not found
                    wrestlerStats.innerHTML = `<p>Error: ${data.error}</p>`;
                } else {
                    // Extract wrestler and championships data
                    const wrestler = data.wrestler;
                    const championships = data.championships;
                    
                    // Populate the wrestlerStats div with wrestler information
                    wrestlerStats.innerHTML = `
                        <img src="${wrestler.image_url}" alt="${wrestler.name}" style="width: 200px; height: auto;">
                        <h2>${wrestler.name}</h2>
                        <p>Finishing Move: ${wrestler.finishing_move}</p>
                        <p>Height: ${wrestler.height_feet}'${wrestler.height_inches}"</p>
                        <p>Weight: ${wrestler.weight_lbs} lbs</p>
                        <p>Championships: ${championships.length > 0 ? championships.join(', ') : 'None'}</p>
                        <button id="playTheme">Play Theme Song</button>
                        <audio id="themeAudio" src="${wrestler.theme_song_url}"></audio>
                    `;
                    
                    // Add click event listener to the "Play Theme Song" button
                    document.getElementById('playTheme').addEventListener('click', () => {
                        const audio = document.getElementById('themeAudio');
                        audio.play();
                    });
                }
            })
            .catch(error => {
                // Handle any errors that occur during the fetch operation
                wrestlerStats.innerHTML = `<p>Error: Unable to fetch wrestler data</p>`;
                console.error('Error:', error);
            });
    });
});