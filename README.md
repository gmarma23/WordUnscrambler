# Word Unscrambler
A simple python project to unscramble strings of chars and form derived words. 

Encode char string to vector based on number of occurrences of each char, resulting in permutations of the same chars having identical vectors. Then map vector to an signature-integer using an injective function approctimation. Distinct integers corespond to distinct vectors and vice versa. 

Use a plain txt wordlist file and transform it to a dictionary with integer-signatures as keys and the list of words from the initial wordlist that have same integer-signature as value. 

Whenever a char string needs to be unscrambled simply get it's integer-signature and search in already mapped wordlist for that integer-signature (dictionary key) and return results list (dictionary value).

Default wordlist txt file `english words.txt` can be found in `%project_dir%/wordlists/plain/` directory <br/> 
Default mapped wordlist dictionary file `english words.json` can be found in `%project_dir%/wordlists/mapped/` directory <br/> 
Default valid chars: `abcdefghijklmnopqrstuvwxyz-`

## How to Use
Run `main.py` and use:

1. `charlist` option to unscramble a single string of chars provided to the program with parameter `-c` (or `--chars`). Additionally parameters `-m` (or `--mapedwordlist`) and `-v` (or `--validchars`) can be used in case of use of a custom mapped wordlist. <br/>

Example: `main.py charlist -c "odg"` should return ['dog', 'god']

2. `file` option to unscramble a multiple strings of chars, one for each line in provided file, with parameter `-p` (or `--path`) for input file path. Additionally parameters `-m` (or `--mapedwordlist`) and `-v` (or `--validchars`) can be used in case of use of a custom mapped wordlist. <br/>

Example: `main.py file -p "%path/to/input/txt/file%"`

3. `map` option to transform a plain txt wordlist file to a mapped dictionary format and export it as json with parameter `-w` (or `--wordlist`). Additionally parameter `-v` (or `--validchars`) can be used to ensure that all words in resulting dictionary are derived by combinations of provided valid characters. <br/>

Example: `main.py map -w "%path/to/wordlist/txt/file%"`

When using a custom mapped wordlist with parameter `-m` (or `--mapedwordlist`), parameter `-v` (or `--validchars`) should also be used to overwrite default valid characters. Using these parameters separately is likely to cause errors.
 
