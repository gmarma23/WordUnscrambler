from word import Word, InvalidChar, EmptyValidCharlist
from wordlist import Wordlist
import os

class WordUnscrambler():
    DEFAULT_OUTPUT_PATH = os.path.join(Wordlist.ROOT_DIR, 'output')

    def __init__(self, custom_mapped_wordlist=None, valid_chars=None):
        self.__mapped_wordlist = Wordlist(custom_mapped_wordlist)
        self.__valid_chars = valid_chars

    def __make_output_path(self):
        if not os.path.exists(self.DEFAULT_OUTPUT_PATH):
            os.makedirs(self.DEFAULT_OUTPUT_PATH)

    def unscramble_word(self, charlist):
        try:
            word = Word(charlist, self.__valid_chars)
        except (InvalidChar, EmptyValidCharlist) as e:
            print(str(e))
            return
        signature = word.get_int_signature()
        result = self.__mapped_wordlist.get_results(signature)
        return result

    def unscramble_words(self, input_path):
        results = []
        try:
            with open(input_path, 'r') as file:
                while (line := file.readline().rstrip()):
                    results.append((line, self.unscramble_word(line)))
        except FileNotFoundError:
            print('Invalid path to input file')
            return

        full_filename, ext = os.path.splitext(input_path)
        filename = f'{full_filename.split("/")[-1]} unscrambled{ext}'
        self.__make_output_path()

        with open(os.path.join(self.DEFAULT_OUTPUT_PATH, filename), 'w') as file:
            for chars, words in results:
                line = f'{chars} --> {words}\n'
                file.write(line)
