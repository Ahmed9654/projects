import spotipy
from spotipy import SpotifyClientCredentials, util
from spotipy import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
import os

'''takes the top 100 songs of a certain year and puts them in spotify playlist'''
year = input('What year you would like to travel?Enter the date in YYYY-MM-DD format: ')
response = requests.get(f'https://www.billboard.com/charts/hot-100/{year}/')
soup = BeautifulSoup(response.text, 'html.parser')
all_songs = soup.select(selector='ul li ul li')
# print(all_songs)
songs = []
for i in all_songs:
    song = i.h3
    if song != None:
        songs.append(song.string.strip())
# # print(songs)

# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
key = os.environ.get("SPOTIPY_CLIENT_ID")
secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/user/your user id",
        client_id=key,
        client_secret=secret,
        show_dialog=True,
        cache_path="token.txt",
        username='Ahmed Salem',
    )
)
songs_url = []
# token = util.prompt_for_user_token('Ahmed Salem', scope='playlist-modify-private')
for i in songs:
    try:
        result = sp.search(i)
        songs_url.append(result['tracks']['items'][0]['external_urls']['spotify'])
    except:
        pass
# for i in result:
#     print(i + '\n')
playlist = sp.user_playlist_create(user='your user id', name=f"{year} Billboard 100", public=False)

sp.playlist_add_items(playlist['id'], songs_url)
