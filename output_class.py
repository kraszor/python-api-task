from word_class import Word
from music_class import Music


"""
The class responsible for handling the output on the terminal for the user
"""


class Output:

    def __init__(self, number):
        self._number = int(number)  # number of words
        self._words_data = []  # the list with full words' data
        self._words = []  # the list of single words
        self._songs = []  # the list of songs' data
        self._word_obj = Word('https://random-words-api.vercel.app/word')
        self._music_obj = Music("")

    # getters for the class' atributes

    def get_number(self):
        return self._number

    def get_words_data(self):
        return self._words_data

    def get_words(self):
        return self._words

    def get_songs(self):
        return self._songs

    def get_word_obj(self):
        return self._word_obj

    def get_muscic_obj(self):
        return self._music_obj

    # setters for the class' atributes

    def set_number(self, new_number):
        self._number = new_number

    def set_words_data(self, new_data):
        self._words_data = new_data

    def set_words(self, new_words):
        self._words = new_words

    def set_songs(self, new_songs):
        self._songs = new_songs

    def set_word_obj(self, url):
        self._word_obj = Word(url)

    def set_music_obj(self, word):
        self._music_obj = Music(word)
