from word_unscrambler import WordUnscrambler, CustomizationError
from wordlist import map_plain_wordlist
import argparse


def parse_args():
    arg_parser = argparse.ArgumentParser(
        prog='Word Unscrambler', 
        description='Unscramble a list of given characters to form words consisting of these characters'
    )

    subparsers = arg_parser.add_subparsers(dest='command')

    charlist_parser = subparsers.add_parser('charlist')
    charlist_parser.add_argument(
        '-c', '--chars', 
        action='store', 
        type=str, 
        required=True, 
        help='string of scrambled chars'
    )

    file_parser = subparsers.add_parser('file')
    file_parser.add_argument(
        '-p', '--path',
        action='store',
        type=str,
        required=True,
        help='path of text file with scrambled words'
    )

    map_parser = subparsers.add_parser('map')
    map_parser.add_argument(
        '-w', '--wordlist',
        action='store',
        type=str,
        required=True,
        help='path of plain wordlist text file'
    )

    for subparser in [charlist_parser, file_parser]:
        subparser.add_argument(
            '-m', '--mappedwordlist', 
            action='store', 
            type=str, 
            default=None,
            help='path of custom mapped wordlist'
        )

    for subparser in [charlist_parser, file_parser, map_parser]:
        subparser.add_argument(
            '-v', '--validchars', 
            action='store', 
            type=str, 
            help='string of custom valid chars'
        )

    return arg_parser.parse_args()


def main():
    args = parse_args()

    if len(vars(args)) == 1:
        return
    elif args.command == 'map':
        map_plain_wordlist(args.wordlist, args.validchars)
    else:
        try:
            unscrambler = WordUnscrambler(args.mappedwordlist, args.validchars)
        except CustomizationError as e:
            print(str(e))
            return
        if args.command == 'charlist':
            result = unscrambler.unscramble_word(args.chars)
            print('\n', result, '\n')
        elif args.command == 'file':
            unscrambler.unscramble_words(args.path)


if __name__ == '__main__':
    main()
        