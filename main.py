from word_unscrambler import WordUnscrambler
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
    charlist_parser.add_argument(
        '-m', '--mappedwordlist', 
        action='store', 
        type=str, 
        help='path of custom mapped wordlist'
    )

    file_parser = subparsers.add_parser('file')
    file_parser.add_argument(
        '-p', '--path',
        action='store',
        type=str,
        required=True,
        help='path of text file with scrambled words'
    )
    file_parser.add_argument(
        '-o', '--output',
        action='store',
        type=str,
        help='path of text file to output unscrambled words'
    )

    map_parser = subparsers.add_parser('map')
    map_parser.add_argument(
        '-w', '--wordlist',
        action='store',
        type=str,
        required=True,
        help='path of plain wordlist text file'
    )

    arg_parser.add_argument(
        '-v', '--validchars', 
        action='store', 
        type=str, 
        help='string of custom valid chars'
    )

    return arg_parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    if args.command == 'charlist':
        pass
    elif args.command == 'file':
        pass
    elif args.command == 'map':
        pass
