# WordListGen
Super Simple Python Word List Generator for Fuzzing and Brute Forcing!
All the word list generation you require, ***Only 35 Lines of Python Code!***

I know what your are thinking. Why create another word list generator?  Well, I needed something very simple I could modify on the fly to get the exact character generators for the task at hand. This script is fully functional in its own right, but intended to be modified during CTF's or pen testing engagements easily *on the fly*.

## Python help documentation:
```
> wordlistgen.py -h
WordListGen: 0.1 Updated: March 22, 2018
usage: wordlistgen.py [-h] [-all] [-lower] [-upper] [-leet] [-swap]
                      [-capitalize] [-orig] [-min MIN] [-max MAX]
                      [-input file] [-output file]

WordListGen - Very Simple Word List Morpher - Creates a list of unique
words for fuzzing / brute forcing

optional arguments:
  -h, --help    show this help message and exit
  -all          Runs all word list morphers
  -lower        Lowercase each word on the input list
  -upper        Uppercase each word on the input list
  -leet         Uppercase each word on the input list
  -swap         Swap the case of the word list
  -capitalize   Capitalize the first letter of the word list
  -orig         Include the original word from the word list
  -min MIN      Minimum word size (default: 3)
  -max MAX      Maximum word size (default: 20)
  -input file   Input wordlist (default: wordlist.txt)
  -output file  Output wordlist (default: wordlistout.txt)

Process finished with exit code 0
```

## Example use and output
```
> wordlistgen.py -all
WordListGen: 0.1 Updated: March 22, 2018
DONE!
 Wordlist input:	wordlist.txt
 Wordlist output:	wordlistout.txt
```
