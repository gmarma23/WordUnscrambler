# Word Unscrambler
A simple python project to unscramble strings of chars and form derived words. 

###### CORE 
Encode char string to vector based on number of occurrences of each char, resulting in permutations of the same chars having identical vectors. 

## Usage
Run `main.py` and use:

1.`charlist` option to unscramble a single string of chars provided to the program with parameter `-c` (or `--chars`). Additionally parameters `-m` or (`--mapedwordlist`) and `-v` (or `--validchars`) can be used in case of use of a custom mapped wordlist. 

2.`file` option to unscramble a multiple strings of chars, one for each line in provided file, with parameter `-p` (or `--path`). Additionally parameters `-m` or (`--mapedwordlist`) and `-v` (or `--validchars`) can be used in case of use of a custom mapped wordlist. 
