import random
import re
import requests

from spotifyApi import BASE_URL


class TrackInfo:
    def __init__(self, info):
        self.info = info

    def get_music_name(self):
        name = self.info['name']

        it_is_not_part_of_the_music_name = [" - Ao Vivo", " - Live", " - Acustico", " - Acoustic", " Version", " Live", " | Acústico", " | Ao Vivo"]

        for invalid_words in it_is_not_part_of_the_music_name:
            if invalid_words in name:
                name = re.sub(invalid_words, "", name)

        return name

    def tip(self):
        name = self.info['name']
        word_with_underscore = ''
        empty = ' '

        for letter in name:
            if letter == empty and len(name) > 3:
                letter = letter.replace(letter, ' ')
            elif letter == name[0] or letter == name[1] or letter == name[3]:
                letter = letter
            else:
                letter = letter.replace(letter, '_')
            word_with_underscore = word_with_underscore + letter + ' '

        return word_with_underscore

    def get_artist_name(self):
        return self.info['album']['artists'][0]['name']

    def get_music_url(self):
        return self.info['preview_url']

    # def get_playlist(auth_header, playlist_id):


#     json_object = requests.get(BASE_URL + 'playlists/' + playlist_id, headers=auth_header)
#     return json_object.json()


class SpotifyApi:

    def __init__(self, client_id, client_secret):
        self.auth = self._login_to_spotify(client_id, client_secret)

    @classmethod
    def _login_to_spotify(cls, client_id, client_secret):
        AUTH_URL = 'https://accounts.spotify.com/api/token'

        auth_response = requests.post(AUTH_URL, {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        })

        auth_response_data = auth_response.json()
        access_token = auth_response_data['access_token']

        headers = {
            'Authorization': 'Bearer {token}'.format(token=access_token)
        }
        return headers

    def get_id_music_in_playlist(self, playlist_id):
        json_object = requests.get(BASE_URL + 'playlists/' + playlist_id, headers=self.auth)
        data = json_object.json()

        ids = []
        for item in data['tracks']['items'][:100]:
            ids.append(item['track']['id'])

        random.shuffle(ids)

        return ids

    def get_track_info(self, track_id):
        json_object = requests.get(BASE_URL + 'tracks/' + track_id, headers=self.auth)
        return TrackInfo(json_object.json())
