from word import Word, InvalidChar
from filesystem import Filesystem
import json


class Wordlist():
    __DEFAULT_MAPPED_WORDLIST_PATH = Filesystem.get_mapped_wordlist_path('english wordlist.json') 
    

    def __init__(self, custom_mapped_wordlist_path: str='') -> None:
        self.__mapped_wordlist = {}
        self.__valid_chars = ''
        self.__load_mapped_wordlist(custom_mapped_wordlist_path)
    

    @staticmethod
    def map_plain_wordlist(wordlist_path: str, valid_chars: str='') -> None:
        """Map plain wordlist entries to their corresponding integer signatures in a 
        dictionary with signatures as keys and list of words as value. All words in 
        provided wordlist must be derived using a combination of provided valid chars."""

        mapped_wordlist = {}
        mapped_wordlist['valid_chars'] = list(valid_chars)
        
        try:
            # Read wordlist entries from txt file
            with open(wordlist_path, 'r') as file:
                # Parse file line by line
                while line := file.readline().rstrip():
                    try:
                        word = Word(line, valid_chars)
                    except InvalidChar as e:
                        print(str(e))
                        continue

                    signature = word.int_signature
                    if signature in mapped_wordlist.keys():
                        # Signature already exists in dictionary
                        mapped_wordlist[signature].append(line)
                    else:
                        # Create new key, value entry in dictionary
                        mapped_wordlist[signature] = [line] 
        except FileNotFoundError:
            print('Invalid path to wordlist txt file')
            return

        # Extract filename from given wordlist txt file path
        wordlist_filename = Filesystem.get_filename_stem(wordlist_path)

        # Export mapped wordlist dictionary as json file for future use
        mapped_wordlist_path = Filesystem.get_mapped_wordlist_path(f'{wordlist_filename}.json')
        with open(mapped_wordlist_path, 'w') as file:
            json.dump(mapped_wordlist, file)


    @property
    def valid_chars(self) -> str:
        return self.__valid_chars


    def signature_query(self, signature: int) -> list[str]:
        """Search for matching words in mapped wordlist"""

        signature = str(signature)
        return self.__mapped_wordlist[signature] if signature in self.__mapped_wordlist else []


    def __load_mapped_wordlist(self, custom_mapped_wordlist_path: str) -> None:
        """Load mapped wordlist dictionary from json file"""

        # Select default file if no custom one is provided
        mapped_wordlist_path = self.__DEFAULT_MAPPED_WORDLIST_PATH if len(custom_mapped_wordlist_path) == 0 else custom_mapped_wordlist_path
        
        try:
            with open(mapped_wordlist_path, 'r') as file:
                self.__mapped_wordlist = json.load(file)
        except FileNotFoundError:
            print('Invalid path to mapped wordlist')
            return
        
        self.__valid_chars = self.__mapped_wordlist['valid_chars']
