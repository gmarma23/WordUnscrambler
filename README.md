# Word Unscrambler
Unscramble provided character strings to form derived words

## Core Implementation

A character string is encoded as a vector holding the number of occurrences of each character in the string, resulting in permutations of the same characters having identical vectors. Then the vector is mapped to a unique signature-integer using an injective function approctimation. Distinct integers corespond to distinct vectors and vice versa. 

A plain txt wordlist file is used to generate a json dictionary with integer-signatures as keys and the list of words from the initial wordlist that have the same integer-signature as value of that key. This action is performed only once for each plain wordlist and the resulting mapped wordlist can be used multiple times from now on.

Whenever a character string needs to be unscrambled, firstly it's integer-signature is calculated and then a search is performed in an already mapped wordlist for that integer-signature as dictionary key. The 
corresponding dictionary value is then returned as the results list, populated with derived words.

Two already mapped wordlists can be found in `%project_dir%/wordlists/mapped/` directory: <br/> 
  - `english_wordlist_simple.json` (DEFAULT MAPPED WORDLIST)<br/>
  - `english_wordlist_complex.json`

## How to Use
Run `main.py` and use:

1. `unscramble` option to unscramble character strings.<br/>
  - Use `--chars` (or `-c`) argument to provide a single character string.<br/>
  - Use `--file` (or `-f`) argument to provide multiple character strings via a txt file (one string per line). The results are outputted inside `%project_dir%/output/` directory as a txt file named `%initial_filename%_unscrambled.txt`.<br/><br/>
Additionally:<br/><br/>
  - Use `--subsets` (or `-s`) argument to unscramble all subsets of provided character string as well.<br/>
  - Use `--wordlist` (or `-w`) argument to provide a path to a custom mapped wordlist. If a custom mapped wordlist is not provided then default english_wordlist_simple.json will be used.<br/><br/>

2. `map` option to generate a custom mapped wordlist.<br/>
  - Use `--wordlist` (or `-w`) argument to specify the path to a plain txt wordlist file.<br/>
  - Use `--valid-chars` (or `-v`) argument to provide a string of characters that are permitted to be present in words of the new custom mapped wordlist. During the creation of a mapped wordlist, a word from the plain wordlist is not registered if it contains invalid characters.

<br/>Examples:<br/><br/>
  
python main.py unscramble -c "ogd"<br/>

ogd --> ['dog', 'god']<br/><br/>
  
python main.py unscramble -c "ogd" -s<br/>
  
og --> ['go']<br/>
od --> ['do']<br/>
ogd --> ['dog', 'god']<br/><br/>

python main.py map -w "%path_to_plain_txt_wordlist%" -v "abcdefghijklmnopqrstuvwxyz-"<br/>
