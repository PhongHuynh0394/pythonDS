from requests import get
import json


class SpotifyScrapper:
    def __init__(self, headers):
        self.headers = headers


def search_for_artist_id(artist_name, headers):
    '''
    Returns the artist id of the first artist found
    '''
    url = "https://api.spotify.com/v1/search"
    params = {"q": artist_name, "type": "artist", "limit": 1}
    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)["artists"]["items"][0]["id"]
    return json_result


def get_artist_albums(artist_id, headers):
    '''
    Returns a list of albums from the artist
    '''
    url = "https://api.spotify.com/v1/artists/" + artist_id + "/albums"
    params = {"include_groups": "album", "limit": 30}
    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)["items"]
    return json_result


def get_songs_from_album(album_id, headers):
    '''
    Returns a list of songs from the album
    '''
    url = "https://api.spotify.com/v1/albums/" + album_id + "/tracks"
    params = {"limit": 50}
    result = get(url, headers=headers, params=params)
    json_result = json.loads(result.content)["items"]
    return json_result


def get_info_of_artist(artist_id, headers):
    '''
    Returns a list of songs from the album
    '''
    url = "https://api.spotify.com/v1/artists/" + artist_id
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    artist_popularity, artist_followers = json_result["popularity"], json_result["followers"]["total"]
    return artist_popularity, artist_followers


def get_info_of_song(song_id, headers):
    '''
    Returns a list of songs from the album
    '''
    url = "https://api.spotify.com/v1/tracks/" + song_id
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    song_name, song_popularity, song_disc_number, song_explicit = json_result[
        "name"], json_result["popularity"], json_result["disc_number"], json_result["explicit"]
    return song_name, song_popularity, song_disc_number, song_explicit


def get_info_of_album(album_id, headers):
    '''
    Returns a list of songs from the album
    '''
    url = "https://api.spotify.com/v1/albums/" + album_id
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    album_type, album_name, album_popularity, album_release_date, album_total_tracks = json_result["album_type"], json_result[
        "name"], json_result["popularity"], json_result["release_date"], json_result["total_tracks"]
    return album_type, album_name, album_popularity, album_release_date, album_total_tracks


def get_info_features_of_song(song_id, headers):
    '''
    Returns a list of songs from the album
    '''
    url = "https://api.spotify.com/v1/audio-features/" + song_id
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    song_danceability, song_energy, song_key, song_loudness, song_mode, song_speechiness, song_acousticness, song_instrumentalness, song_liveness, song_valence, song_tempo, song_duration_ms, song_time_signature = json_result[
        "danceability"], json_result["energy"], json_result["key"], json_result["loudness"], json_result["mode"], json_result["speechiness"], json_result["acousticness"], json_result["instrumentalness"], json_result["liveness"], json_result["valence"], json_result["tempo"], json_result["duration_ms"], json_result["time_signature"]
    return song_danceability, song_energy, song_key, song_loudness, song_mode, song_speechiness, song_acousticness, song_instrumentalness, song_liveness, song_valence, song_tempo, song_duration_ms, song_time_signature