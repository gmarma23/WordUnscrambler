from word import Word, InvalidChar, EmptyValidCharlist
import json
import os


class Wordlist():
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    DEFAULT_MAPPED_DIR = os.path.join(ROOT_DIR, 'wordlists', 'mapped')
    DEFAULT_MAPPED_WORDLIST = os.path.join(DEFAULT_MAPPED_DIR, 'english wordlist.json')
    
    def __init__(self, custom_mapped_wordlist=None):
        self.__mapped_wordlist = {}
        self.__load_mapped_wordlist(custom_mapped_wordlist)
    
    @staticmethod
    def map_plain_wordlist(path_to_txt, valid_chars=None):
        # Map plain wordlist entries to their corresponding integer signatures
        # to a dictionary with signatures as keys and list of words as value  
        mapped_wordlist = {}
        try:
            # Read wordlist entries from txt file
            with open(path_to_txt, 'r') as file:
                # Parse file line by line
                while (line := file.readline().rstrip()):
                    word = Word(line, valid_chars)
                    signature = word.get_int_signature()
                    if signature in mapped_wordlist.keys():
                        # Signature already exists in dictionary, 
                        # append new word in value list 
                        mapped_wordlist[signature].append(line)
                    else:
                        # Create new key, value entry in dictionary
                        mapped_wordlist[signature] = [line] 
        except FileNotFoundError:
            print('Invalid path to plain wordlist')
            return
        except (InvalidChar, EmptyValidCharlist) as e:
            print(str(e))
            return

        # Extract filename from given wordlist txt file path
        full_filename,_ = os.path.splitext(path_to_txt)
        filename = full_filename.split('\\')[-1]

        # Export mapped wordlist dictionary as json file for future use
        with open(os.path.join(Wordlist.DEFAULT_MAPPED_DIR, f'{filename}.json'), 'w') as file:
            json.dump(mapped_wordlist, file)

    def __load_mapped_wordlist(self, custom_mapped_wordlist):
        # Load mapped wordlist dictionary from json file
        # Select default file if no custom one is provided
        mapped_wordlist_location = custom_mapped_wordlist if custom_mapped_wordlist else self.DEFAULT_MAPPED_WORDLIST
        try:
            with open(mapped_wordlist_location, 'r') as file:
                self.__mapped_wordlist = json.load(file)
        except FileNotFoundError:
            print('Invalid path to mapped wordlist')
            return

    def get_results(self, signature):
        # Return list of matched words or empty list 
        signature = str(signature)
        if signature in self.__mapped_wordlist:
            return self.__mapped_wordlist[signature]
        else:
            return []


# Module level alias for static function to avoid importing the whole class to call this function
# Alternative Python solution to Java's "import static"
map_plain_wordlist = Wordlist.map_plain_wordlist
