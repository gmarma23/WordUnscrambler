from word import Word, InvalidChar
from wordlist import Wordlist
from filesystem import Filesystem
import itertools


class WordUnscrambler():
    def __init__(self, custom_mapped_wordlist: str='') -> None:
        self.__mapped_wordlist = Wordlist(custom_mapped_wordlist)


    def unscramble_word(self, charlist: str, check_charlist_subsets: bool) -> dict[str, list[str]]:
        """Unscramble provided string of chars to form derived words"""

        results = {}
        min_charlist_length = 2 if check_charlist_subsets else len(charlist)
        charlist_subset_signatures = []
        
        for i in range(min_charlist_length, len(charlist)+1):
            for charlist_subset in itertools.combinations(charlist, i):
                charlist_subset_str = ''.join(charlist_subset)

                try:
                    word = Word(charlist_subset_str, self.__mapped_wordlist.valid_chars)
                except InvalidChar as e:
                    print(str(e))
                    exit()
                
                signature = word.int_signature
                if signature in charlist_subset_signatures:
                    continue

                matches = self.__mapped_wordlist.signature_query(signature)
                if len(matches):
                    results[charlist_subset_str] = self.__mapped_wordlist.signature_query(signature)

        return results


    def unscramble_words(self, input_file_path: str, check_charlist_subsets: bool) -> None:
        """Unscramble multiple words from input txt file entries and export results in txt file"""

        results = []

        try:
            with open(input_file_path, 'r') as file:
                while line := file.readline().rstrip():
                    results.append((line, self.unscramble_word(line, check_charlist_subsets)))
        except FileNotFoundError:
            print('Invalid path to input file')
            exit()

        filename = Filesystem.get_filename_stem(input_file_path)
        file_suffix = Filesystem.get_filename_suffix(input_file_path)
        output_path = Filesystem.get_output_file_path(f'{filename}_unscrambled{file_suffix}')

        with open(output_path, 'w') as file:
            for chars, result in results:
                block_title = f"{chars}\n{len(chars)*'='}\n"
                file.write(block_title)

                for chars_subset, matches in result.items():
                    result_line = f'\t{chars_subset} --> {matches}\n'
                    file.write(result_line)

                file.write('\n')
    

    def print_single_word_results(self, result: dict[str, list[str]]) -> None:
        """Output unscrambled word result dictionary in terminal"""

        for chars_subset, matches in result.items():
            result_line = f'\t{chars_subset} --> {matches}\n'
            print(result_line, end='')