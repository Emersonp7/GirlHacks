document.getElementById('myBtn').addEventListener('click', function() {
    const clientId = '4c9e4fb01bd345989368485e373fcc19';
    const redirectUri = 'https://localhost:3000/callback';
<<<<<<< HEAD
    const scopes = 'user-read-private user-read-email';
=======
    const scopes = 'user-read-private user-read-email user-top-read';
>>>>>>> f6256b91d556f6a20b9c56d779549a3e376e3c56

    const authUrl = `https://accounts.spotify.com/authorize?response_type=code&client_id=${clientId}&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(redirectUri)}`;

    window.location.href = authUrl;
});

window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('code')) {
        // Fetch top artists data from Flask server
        fetch('https://localhost:3000/top-artists')
            .then(response => response.json())
            .then(artists => {
                // Store the top artists data in localStorage
                localStorage.setItem('topArtists', JSON.stringify(artists));
                // Redirect to final.html
                window.location.href = 'final.html';
            })
            .catch(error => console.error('Error fetching top artists:', error));
    }
};