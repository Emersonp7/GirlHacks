document.getElementById('myBtn').addEventListener('click', function() {
    const clientId = '4c9e4fb01bd345989368485e373fcc19'; // Replace with your actual Client ID
    const redirectUri = 'localhost:3000'; // Replace with your actual Redirect URI
    const scopes = 'user-read-private user-read-email'; // Add any other scopes you need

    const authUrl = `https://accounts.spotify.com/authorize?response_type=code&client_id=${clientId}&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(redirectUri)}`;

    window.location.href = authUrl;
});