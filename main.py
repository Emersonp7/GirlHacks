import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

clientId = "4c9e4fb01bd345989368485e373fcc19"
clientSecret = "f56247ad580b433681d4edadccef32f6"

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret))

