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

    def get_music_obj(self):
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

    # getting n random words, where n equals the number entered by the user

    def get_num_words(self):
        i = 0
        words_data = self.get_words_data()
        words = self.get_words()
        word = self.get_word_obj()
        while i < self.get_number():
            word.get_word_data()
            if str(word) not in words_data:
                words_data.append(str(word))
                words.append(word.get_word())
                i += 1
            else:
                continue

    def display_random_words(self):
        for elem in self.get_words_data():
            print(elem)

    # getting song for words collected in list

    def get_music_from_word(self):
        songs_list = self.get_songs()
        words_list = sorted(self.get_words())
        i = 0
        while i < len(words_list):
            self.set_music_obj(words_list[i])
            music = self.get_music_obj()
            try:
                music.get_music_from_word(0)
                if str(music) not in songs_list:
                    songs_list.append(str(music))
                    i += 1
                else:
                    continue
            except IndexError:
                songs_list.append("No recording found!\n")
                i += 1

    # creating a string representation of an object

    def __str__(self):
        words = sorted(self.get_words())
        songs = self.get_songs()
        txt = ""
        for i in range(0, len(words)):
            txt += words[i] + "\n"
            txt += "A song with the above word in title:\n"
            txt += songs[i] + "\n"
        return txt
