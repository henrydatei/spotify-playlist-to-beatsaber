# spotify-playlist-to-beatsaber
A Python script that fetches a Spotify playlist and searches on [https://beatsaver.com](https://beatsaver.com) for the songs + downloads them if found

### Usage
Install required packages:
```
pip install requests spotipy
```
Create a new app on [https://developers.spotify.com/](https://developers.spotify.com/) and copy client ID and client secret in the file [spotify_beatsaver.py](https://github.com/henrydatei/spotify-playlist-to-beatsaber/blob/main/spotify_beatsaver.py) in line [44 and 45](https://github.com/henrydatei/spotify-playlist-to-beatsaber/blob/main/spotify_beatsaver.py#L44)

Search for a playlist on Spotify (e.g. [https://open.spotify.com/playlist/37i9dQZF1DX7ZUug1ANKRP](https://open.spotify.com/playlist/37i9dQZF1DX7ZUug1ANKRP)) and get the ID of this playlist (e.g. 37i9dQZF1DX7ZUug1ANKRP). Insert this ID in [line 49](https://github.com/henrydatei/spotify-playlist-to-beatsaber/blob/main/spotify_beatsaver.py#L49).

Set the path for custom songs in BeatSaber in [line 8](https://github.com/henrydatei/spotify-playlist-to-beatsaber/blob/main/spotify_beatsaver.py#L8).

Run the script
```
python3 spotify_beatsaver.py
```
