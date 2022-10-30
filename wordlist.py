from word import Word, InvalidChar, EmptyValidCharlist
import json
import os


class Wordlist():
    ROOT_DIR = os.path.dirname(os.path.realpath(__file__))
    DEFAULT_MAPPED_DIR = os.path.join(ROOT_DIR, 'wordlists', 'mapped')
    DEFAULT_MAPPED_WORDLIST = os.path.join(DEFAULT_MAPPED_DIR, 'english wordlist.json')
    
    def __init__(self, mapped_wordlist=None):
        self.__mapped_wordlist = self.DEFAULT_MAPPED_WORDLIST
    
    @staticmethod
    def map_plain_wordlist(path_to_txt, valid_chars=None):
        mapped_wordlist = {}
        c = 0
        try:
            with open(path_to_txt, 'r') as file:
                while (line := file.readline().rstrip()):
                    word = Word(line, valid_chars)
                    signature = word.get_int_signature()
                    if signature in mapped_wordlist.keys():
                        mapped_wordlist[signature].append(line)
                    else:
                        mapped_wordlist[signature] = [line] 
                    c += 1
        except FileNotFoundError:
            print('Invalid path to txt file')
            return
        except (InvalidChar, EmptyValidCharlist) as e:
            print(str(e))
            return

        full_filename,_ = os.path.splitext(path_to_txt)
        filename = full_filename.split('\\')[-1]
        with open(os.path.join(Wordlist.DEFAULT_MAPPED_DIR, f'{filename}.json'), 'w') as file:
            json.dump(mapped_wordlist, file)
