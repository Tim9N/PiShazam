function fetchSongData() {
    var timestamp = new Date().getTime();
    var imageUrl = 'res/cover.jpg?' + timestamp;
    var jsonUrl = 'res/song_info.json?' + timestamp; 

    // Use fetch API to load the JSON file
    fetch(jsonUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok for song_info.json');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('album-cover').src = imageUrl;
            document.getElementById('song-title').textContent = data.title || 'Title not found';
            document.getElementById('song-artist').textContent = data.artist || 'Artist not found';
            document.getElementById('song-album').textContent = data.album || 'Album not found';
            document.getElementById('song-lyrics').textContent = data.lyrics || 'Lyrics not found';
        })
        .catch(error => {
            console.error('Error fetching song data:', error);
        });
}

// Update the song data every 1 seconds
setInterval(fetchSongData, 1000);

// Fetch the initial song data on page load
fetchSongData();
