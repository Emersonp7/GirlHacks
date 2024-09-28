import spotipy
from spotipy.oauth2 import SpotifyOAuth

clientId = "4c9e4fb01bd345989368485e373fcc19"
clientSecret = "f56247ad580b433681d4edadccef32f6"
redirectUri = "https://localhost:3000/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, 
                                               client_secret=clientSecret, 
                                                redirect_uri=redirectUri, 
                                                scope="user-top-read"))

tracks = sp.current_user_top_tracks(limit=10)

print(tracks)