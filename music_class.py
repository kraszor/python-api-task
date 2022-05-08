import requests
import sys


"""
The class responisible for handling MusicBrainz REST API
"""


class Music:

    def __init__(self, word):
        self._word = word
        self._api_url = \
            "http://musicbrainz.org/ws/2/recording/" + \
            f"?query=recording:{word}&fmt=json"
        self._artitst = ""
        self._title = ""
        self._album = ""

    # getters for the class atributes

    def get_word(self):
        return self._word

    def get_api_url(self):
        return self._api_url

    def get_artist(self):
        return self._artitst

    def get_title(self):
        return self._title

    def get_album(self):
        return self._album

    # setters for the class atributes

    def set_word(self, new_word):
        self._word = new_word

    def set_api_url(self, new_api_url):
        self._api_url = new_api_url

    def set_artist(self, new_artist):
        self._artitst = new_artist

    def set_title(self, new_title):
        self._title = new_title

    def set_album(self, new_album):
        self._album = new_album

    def get_music_from_word(self, index):
        try:
            r = requests.get(self.get_api_url()).json()['recordings']
            r = r[index]
            self.set_title(r['title'])
            self.set_artist(r['artist-credit'][0]['name'])
            self.set_album(r['releases'][0]['title'])
        # critical error, the program can't work with invalid API's URL
        except (requests.exceptions.RequestException, KeyError):
            print("Invalid API's URL error!")
            sys.exit()

    # creating a string representation of an object

    def __str__(self):
        info = """
                Title: {}\n
                Artist: {}\n
                Album: {}\n
               """.format(self.get_title(),
                          self.get_artist(),
                          self.get_album())
        return info
