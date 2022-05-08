import requests


"""
The class responsilbe for handling random words api
"""


class Word:

    def __init__(self, api_url):
        self._api_url = api_url
        self._word = ""
        self._definition = ""
        self._pronunciation = ""

    # getters for class attributes

    def get_api_url(self):
        return self._api_url

    def get_word(self):
        return self._word

    def get_definition(self):
        return self._definition

    def get_pronunciation(self):
        return self._pronunciation

    # setters for class attributes

    def set_api_url(self, new_api_url):
        self._api_url = new_api_url

    def set_word(self, new_word):
        self._word = new_word

    def set_definition(self, new_def):
        self._definition = new_def

    def set_pronunciation(self, new_pronun):
        self._pronunciation = new_pronun
