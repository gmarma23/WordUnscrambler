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
        mapped_wordlist = {}
        try:
            with open(path_to_txt, 'r') as file:
                while (line := file.readline().rstrip()):
                    word = Word(line, valid_chars)
                    signature = word.get_int_signature()
                    if signature in mapped_wordlist.keys():
                        mapped_wordlist[signature].append(line)
                    else:
                        mapped_wordlist[signature] = [line] 
        except FileNotFoundError:
            print('Invalid path to plain wordlist')
            return
        except (InvalidChar, EmptyValidCharlist) as e:
            print(str(e))
            return

        full_filename,_ = os.path.splitext(path_to_txt)
        filename = full_filename.split('\\')[-1]
        with open(os.path.join(Wordlist.DEFAULT_MAPPED_DIR, f'{filename}.json'), 'w') as file:
            json.dump(mapped_wordlist, file)

    def __load_mapped_wordlist(self, custom_mapped_wordlist):
        mapped_wordlist_location = custom_mapped_wordlist if custom_mapped_wordlist else self.DEFAULT_MAPPED_WORDLIST
        try:
            with open(mapped_wordlist_location, 'r') as file:
                self.__mapped_wordlist = json.load(file)
        except FileNotFoundError:
            print('Invalid path to mapped wordlist')
            return

    def get_results(self, signature):
        signature = str(signature)
        if signature in self.__mapped_wordlist:
            return self.__mapped_wordlist[signature]
        else:
            return []
