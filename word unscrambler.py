from wordlist import Wordlist
from word import Word
import argparse


def parse_args():
    arg_parser = argparse.ArgumentParser(prog='Word Unscrambler', description='Unscramble a list of given characters to form words consisting of these characters')
    arg_parser.add_argument('-c', '--charlist', action='store', type=str, required=True, help='get list of scrambled chars')
    arg_parser.add_argument('--mappedWordlist', action='store', type=str, default=None, help='get path of custom mapped wordlist')
    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    word = Word(args.charlist)
    wordlist = Wordlist(args.mappedWordlist)

    print(args.charlist, '-->', wordlist.get_results(word.get_int_signature()))
