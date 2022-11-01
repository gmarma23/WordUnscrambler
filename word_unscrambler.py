from word import Word, InvalidChar, EmptyValidCharlist
from wordlist import Wordlist
import os


class WordUnscrambler():
    # Path to export txt file with multiple unscrambled words 
    DEFAULT_OUTPUT_PATH = os.path.join(Wordlist.ROOT_DIR, 'output')

    def __init__(self, custom_mapped_wordlist=None, valid_chars=None):
        if bool(custom_mapped_wordlist) ^ bool(valid_chars):
            raise CustomizationError()
        self.__mapped_wordlist = Wordlist(custom_mapped_wordlist)
        self.__valid_chars = valid_chars

    def __make_output_path(self):
        # Utility function to create output path if not already present
        if not os.path.exists(self.DEFAULT_OUTPUT_PATH):
            os.makedirs(self.DEFAULT_OUTPUT_PATH)

    def unscramble_word(self, charlist):
        # Unscramble single word from provided string of chars 
        try:
            word = Word(charlist, self.__valid_chars)
        except (InvalidChar, EmptyValidCharlist) as e:
            print(str(e))
            return
        signature = word.get_int_signature()
        result = self.__mapped_wordlist.get_results(signature)
        return result

    def unscramble_words(self, input_path):
        # Unscramble multiple words from input txt 
        # file entries and export results in txt file  
        results = []
        try:
            # Read input file entries 
            with open(input_path, 'r') as file:
                # Parse file line by line
                while (line := file.readline().rstrip()):
                    # Append tuple (charlist, words) in results list
                    results.append((line, self.unscramble_word(line)))
        except FileNotFoundError:
            print('Invalid path to input file')
            return

        # Extract filename from provided input txt file path 
        full_filename, ext = os.path.splitext(input_path)
        filename = f'{full_filename.split("/")[-1]} unscrambled{ext}'
        self.__make_output_path()

        # Export results list in txt file in output directory 
        # named "%input_file_name% unscrambled.txt"
        with open(os.path.join(self.DEFAULT_OUTPUT_PATH, filename), 'w') as file:
            for chars, words in results:
                line = f'{chars} --> {words}\n'
                file.write(line)


class CustomizationError(Exception):
    def __init__(self):            
        super().__init__(
            'Custom mapped wordlist and valid char list should both\n' + \
            'be defined accordingly or be left to their default values\n' + \
            '(Custom valid char list set forms all words in provided mapped wordlist)'
        )
