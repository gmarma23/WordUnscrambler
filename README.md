# Word Unscrambler
Unscramble provided character strings to form derived words

## Core Implementation

A character string is encoded as a vector holding the number of occurrences of each character in the string, resulting in permutations of the same characters having identical vectors. Then the vector is mapped to a unique signature-integer using an injective function approctimation. Distinct integers corespond to distinct vectors and vice versa. 

A plain txt wordlist file is used to generate a json dictionary with integer-signatures as keys and the list of words from the initial wordlist that have the same integer-signature as value of that key. This action is performed only once for each plain wordlist and the resulting mapped wordlist can be used multiple times from now on.

Whenever a character string needs to be unscrambled, firstly it's integer-signature is calculated and then a search is performed in an already mapped wordlist for that integer-signature as dictionary key. The 
corresponding dictionary value is then returned as the results list, populated with derived words.

Two already mapped wordlists can be found in `%project_dir%/wordlists/mapped/` directory: <br/> 
  - english_wordlist_simple.json (DEFAULT WORDLIST)<br/>
  - english_wordlist_complex.json

## How to Use
Run `main.py` and use:

1. `unscramble` option to unscramble character strings.<br/><br/>
  - Use `--chars` (or `-c`) argument to provide a single character string.<br/>
  - Use `--file` (or `-f`) argument to provide multiple character strings via a txt file (one string per line).<br/><br/>
  Additionally:<br/><br/>
  - Use `--subsets` (or `-s`) argument to unscramble all subsets of provided character string as well.<br/>
  - Use `--wordlist` (or `-w`) argument to provide a path to a custom mapped wordlist.<br/> 

Examples: <br/>
