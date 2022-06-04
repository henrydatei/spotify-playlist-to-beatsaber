import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests

def searchOnBeatsaver(artist, title, maxResults = 1, minScore = 0.6):
    query = artist + " " + title
    params = {"q": query, "sortOrder": "Relevance"}
    req = requests.get("https://api.beatsaver.com/search/text/0", params = params)
    req.raise_for_status()
    for i, song in enumerate(req.json()["docs"]):
        if i < maxResults:
            score = song["stats"]["score"]
            hash = song["versions"][0]["hash"]
            name = song["name"]
            if score > minScore:
                return True, hash, name
            else:
                return False, hash, name

def searchOnSpotify(query):
    result = sp.search(query, limit = 1, type = "track")
    title = result["tracks"]["items"][0]["name"].split("(")[0].split(" - ")[0]
    artists = [artist["name"] for artist in result["tracks"]["items"][0]["artists"]]
    return title, artists

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id="your client id",
                                                 client_secret="your client secret",
                                                 redirect_uri="http://localhost:8080",
                                                 scope="user-library-read"))

results = sp.playlist_tracks('spotify:playlist:37i9dQZF1DX7ZUug1ANKRP')
for item in results["items"]:
    artists = [artist["name"] for artist in item["track"]["album"]["artists"]]
    name = item["track"]["name"]
    firstArtist = artists[0]
    title = name.split("(")[0].split(" - ")[0]
    try:
        bool, hash, name = searchOnBeatsaver(firstArtist, title)
        if bool:
            BSTitle, BSArtists = searchOnSpotify(name)
            artistsTheSame = False
            for artist in artists:
                if artist in BSArtists:
                    artistsTheSame = True
            if title == BSTitle and artistsTheSame:
                print(title, artists, hash)
    except:
        pass
