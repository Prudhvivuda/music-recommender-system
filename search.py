import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_info(artist, track):
    results = sp.search(q=f'artist:{artist} track:{track}', type='track')

    if results['tracks']['items']:
        track_info = results['tracks']['items'][0]
        track_name = track_info['name']
        artists = ', '.join([artist['name'] for artist in track_info['artists']])
        album_name = track_info['album']['name']
        release_date = track_info['album']['release_date']
        duration_ms = track_info['duration_ms']
        popularity = track_info['popularity']
        
        print(f'Track Name: {track_name}')
        print(f'Artists: {artists}')
        print(f'Album: {album_name}')
        print(f'Release Date: {release_date}')
        print(f'Duration: {duration_ms} milliseconds')
        print(f'Popularity: {popularity}')
    else:
        print('Track not found.')
    print(results)
    # print(json.dumps(results, indent=4))

# artist_name = input("Enter the artist's name: ")
# track_title = input("Enter the track's title: ")

artist_name = "Andrew Bird" #"Guano Apes" #"Cartola"
track_title = "Heretics (early version)" #"Crossing The Deadline" #"Tive Sim"

get_song_info(artist_name, track_title)
