from word_unscrambler import WordUnscrambler
from wordlist import Wordlist
import argparse


def parse_args():
    arg_parser = argparse.ArgumentParser(
        prog='Word Unscrambler', 
        description='Unscramble a list of given characters to form words consisting of these characters'
    )

    subparsers = arg_parser.add_subparsers(dest='command')

    unscramble_parser = subparsers.add_parser('unscramble')
    input = unscramble_parser.add_mutually_exclusive_group(required=True)
    input.add_argument(
        '-c', '--chars', 
        action='store', 
        type=str, 
        default='',
        help='String of scrambled chars'
    )
    input.add_argument(
        '-f', '--file',
        action='store',
        type=str,
        default='',
        help='Path to text file with scrambled chars (one string per line)'
    )
    unscramble_parser.add_argument(
        '-s', '--subsets', 
        action = 'store_true', 
        required = False, 
        default = False,
        help = 'Additionally, unscramble all subsets of provided scrambled chars'
    )
    unscramble_parser.add_argument(
        '-w', '--wordlist', 
        action='store', 
        type=str, 
        default='',
        required=False,
        help='Path to custom mapped wordlist'
    )

    map_parser = subparsers.add_parser('map')
    map_parser.add_argument(
        '-w', '--wordlist',
        action='store',
        type=str,
        required=True,
        help='Path to plain wordlist text file'
    )
    map_parser.add_argument(
        '-v', '--valid-chars', 
        action='store', 
        type=str, 
        required=False,
        help='String of custom valid chars'
    )

    return arg_parser.parse_args()


def main():
    args = parse_args()

    if len(vars(args)) == 1:
        return
    
    if args.command == 'map':
        Wordlist.map_plain_wordlist(args.wordlist, args.valid_chars)
        return
    
    unscrambler = WordUnscrambler(args.wordlist)

    if args.chars:
        results = unscrambler.unscramble_word(args.chars, args.subsets)
        print()
        unscrambler.print_single_word_results(results)
        print()
    else:
        unscrambler.unscramble_words(args.file, args.subsets)


if __name__ == '__main__':
    main()
        