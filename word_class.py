import requests
import sys


"""
The class responsilbe for handling random words api
"""


class Word:

    def __init__(self, api_url):
        self._api_url = api_url
        self._word = ""
        self._definition = ""
        self._pronunciation = ""

    # getters for the class attributes

    def get_api_url(self):
        return self._api_url

    def get_word(self):
        return self._word

    def get_definition(self):
        return self._definition

    def get_pronunciation(self):
        return self._pronunciation

    # setters for the class attributes

    def set_api_url(self, new_api_url):
        self._api_url = new_api_url

    def set_word(self, new_word):
        self._word = new_word

    def set_definition(self, new_def):
        self._definition = new_def

    def set_pronunciation(self, new_pronun):
        self._pronunciation = new_pronun

    # getting words' data from the api

    def get_word_data(self):
        try:
            r = requests.get(self.get_api_url()).json()
            self.set_word(r[0]["word"])
            self.set_definition(r[0]["definition"])
            self.set_pronunciation(r[0]["pronunciation"])
        # critical error, the program can't work with invalid API's URL
        except (requests.exceptions.RequestException, KeyError):
            print("Invalid API's URL error!")
            sys.exit()

    # creating a string representation of an object

    def __str__(self):
        info = """
                Word: {}\n
                Definition: {}\n
                Pronunciation: {}\n
               """.format(self.get_word(),
                          self.get_definition(),
                          self.get_pronunciation())
        return info
