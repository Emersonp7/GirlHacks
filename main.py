import spotipy
from spotipy.oauth2 import SpotifyOAuth

clientId = "4c9e4fb01bd345989368485e373fcc19"
clientSecret = "f56247ad580b433681d4edadccef32f6"
redirectUri = "https://localhost:3000/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientId, 
                                               client_secret=clientSecret, 
                                                redirect_uri=redirectUri, 
                                                scope="user-top-read"))

artists = sp.current_user_top_artists(limit=50)

# Tracks["items"][index]["name"]
# Index is index of songs in the list


class Spotify:
    def __init__(self, clientID, clientSecret, redirectUrl, scope) -> None:
        self.clientID = clientID
        self.clientSecret = clientSecret
        self.redirectUrl = redirectUrl
        self.scope = scope
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID, 
                                               client_secret=clientSecret, 
                                                redirect_uri=redirectUrl, 
                                                scope=scope))
    def getTopTracks(self, limit) -> list[str]:
        tracks = self.sp.current_user_top_tracks(limit=limit)
        tracklist = []
        for i in range(len(tracks["items"])):
            tracklist.append(tracks["items"][i]["name"])
        return tracklist
    def getTopArtists(self, limit) -> list[str]:
        artists = self.sp.current_user_top_artists(limit=limit)
        artistlist = []
        for i in range(len(artists["items"])):
            artistlist.append(artists["items"][i]["name"])
        return artistlist


# spotify = Spotify(clientId, clientSecret, redirectUri, "user-top-read")
# print(spotify.getTopTracks(5))
# print(spotify.getTopArtists(5))