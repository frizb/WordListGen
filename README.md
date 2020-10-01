# WordListGen
Super Simple Python Word List Generator for Password Cracking (Hashcat)!
It is very useful for a programer

I know what your are thinking. Why create another word list generator?  Well, I needed something very simple I could modify on the fly to get the exact character generators for the task at hand. This script is fully functional in its own right, but intended to be modified during CTF's or pen testing engagements easily *on the fly*.

## Python help documentation:
```
> wordlistgen.py -h
WordListGen: 0.2 Updated: June 2, 2019
usage: wordlistgen.py [-h] [-all] [-lower] [-upper] [-leet] [-swap] [-ntlm]
                      [-baseword] [-capitalize] [-orig] [-min MIN] [-max MAX]
                      [-inputfolder file] [-input file] [-output file]

WordListGen - Very Simple Word List Morpher - Creates a list of unique
words for fuzzing / brute forcing

optional arguments:
  -h, --help         show this help message and exit
  -all               Runs all word list morphers
  -lower             Lowercase each word on the input list
  -upper             Uppercase each word on the input list
  -leet              Leetspeak each word on the input list
  -swap              Swap the case of the word list
  -ntlm              Parse an NTLM Hash dump list for plaintext words to use
                     in a wordlist
  -baseword          Base words only (Post-process) Strips any numbers or
                     symbols from the generated word list
  -capitalize        Capitalize the first letter of the word list
  -orig              Include the original word from the word list
  -min MIN           Minimum word size (default: 4)
  -max MAX           Maximum word size (default: 32)
  -inputfolder file  Specify a folder of wordlists to crawl, process and
                     combine
  -input file        Input wordlist (default: wordlist.txt)
  -output file       Output wordlist (default: wordlistout.txt)
```

## Example use and output
```
> wordlistgen.py -all
WordListGen: 0.2 Updated: June 2, 2019
DONE!
 Wordlist input:	wordlist.txt
 Wordlist output:	wordlistout.txt
```
