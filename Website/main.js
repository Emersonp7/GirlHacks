document.getElementById('myBtn').addEventListener('click', function() {
    const clientId = '4c9e4fb01bd345989368485e373fcc19'; 
    const redirectUri = 'https://localhost:3000/callback';
    const scopes = 'user-read-private user-read-email';

    const authUrl = `https://accounts.spotify.com/authorize?response_type=code&client_id=${clientId}&scope=${encodeURIComponent(scopes)}&redirect_uri=${encodeURIComponent(redirectUri)}`;

    window.location.href = authUrl;
});
window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('code')) {
        window.location.href = 'checkout.html';
    }
};