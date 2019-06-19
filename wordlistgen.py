import argparse
import re
import os
from string import maketrans
input_lines = []
new_word_list = []
post_processed_word_list = []

leet_trans = ["aeiotsbzAEIOTSBZ","4310758243107582","altsALTS","@!+$@!+$"]

print('\033[0;32m'+"WordListGen: " + '0.2' + " Updated: " + 'June 2, 2019'+'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'WordListGen - Very Simple Word List Morpher - Creates a list of unique words for fuzzing / brute forcing'+'\033[0;39m')
parser.add_argument("-all", action='store_true', help='Runs all word list morphers')
parser.add_argument("-lower", action='store_true', help='Lowercase each word on the input list')
parser.add_argument("-upper", action='store_true', help='Uppercase each word on the input list')
parser.add_argument("-leet", action='store_true', help='Leetspeak each word on the input list')
parser.add_argument("-swap", action='store_true', help='Swap the case of the word list')
parser.add_argument("-ntlm", action='store_true', help='Parse an NTLM Hash dump list for plaintext words to use in a wordlist')
parser.add_argument("-baseword", action='store_true', help='Base words only (Post-process) Strips any numbers or symbols from the generated word list')
parser.add_argument("-capitalize", action='store_true', help='Capitalize the first letter of the word list')
parser.add_argument("-orig", action='store_true', help='Include the original word from the word list')
parser.add_argument("-min", type=int, default="4", help='Minimum word size (default: %(default)s)')
parser.add_argument("-max", type=int, default="32", help='Maximum word size (default: %(default)s)')
parser.add_argument("-inputfolder", metavar='file', type=str, help='Specify a folder of wordlists to crawl, process and combine')
parser.add_argument("-input", metavar='file', type=str, default="wordlist.txt", help='Input wordlist (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="wordlistout.txt", help='Output wordlist (default: %(default)s)')

args = parser.parse_args()

if args.inputfolder is not None:
    print "Importing all files in folder: " + args.inputfolder
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(args.inputfolder):
        for file in f:
            #if '.txt' in file:
            files.append(os.path.join(r, file))
    for f in files:
        print("\t"+f)
        with open(f, "r") as filein:
            input_lines += filein.readlines()

else:
    with open(args.input, "r") as filein:
        input_lines = filein.readlines()

for line in input_lines:
    if ( len(line) < args.min or len(line) > args.max ): continue
    if (args.lower or args.all): new_word_list.append(line.lower())
    if (args.upper or args.all): new_word_list.append(line.upper())
    if (args.leet or args.all): new_word_list.append(line.translate(maketrans(leet_trans[0], leet_trans[1])))
    if (args.leet or args.all): new_word_list.append(line.translate(maketrans(leet_trans[2], leet_trans[3])))
    if (args.leet or args.all): new_word_list.append(line.translate(maketrans(leet_trans[2], leet_trans[3])).translate(maketrans(leet_trans[0], leet_trans[1])))
    if (args.swap or args.all): new_word_list.append(line.swapcase())
    if (args.ntlm or args.all):
        results = re.findall(r"\\([\w\.\_\-]{2-32})\$*\:", line)
        if len(results)>0: new_word_list.append(results[0])    # Username with domain prefix
        results = re.findall(r"([\w\.\_\-]{2-32})\$*\:", line)
        if len(results) > 0: new_word_list.append(results[0])  # Match username no domain prefix
        results = re.findall(r"([\w\.\_\-]{2-32})\\", line)
        if len(results) > 0: new_word_list.append(results[0])  # Domain name
    if (args.capitalize or args.all): new_word_list.append(line.title())
    if (args.orig or args.all): new_word_list.append(line)

# Post processing for base word
if args.baseword:
    for line in new_word_list:
        line = re.sub(r'^[^a-zA-Z ]+', "", line)  # remove prefix non-letter chars
        line = re.sub(r'[^a-zA-Z ]+$', "", line)  # remove postfix non-letter chars
        #results = re.findall(r"([A-Za-z\s]{4,})", line)
        #if len(results) > 0: post_processed_word_list.append(results[0])
        post_processed_word_list.append(line + "\n")  # we lose the newline after we remove non-word chars :P
    new_word_list = post_processed_word_list

with open(args.output,"w") as fileout:
    fileout.writelines(sorted(list(set(new_word_list))))
print '\033[0;34m'+"DONE!\n "+'\033[0;33m'+"Wordlist input:\t"+'\033[0;39m'+args.input+"\n"+'\033[0;33m'+" Wordlist output:\t"+'\033[0;39m'+args.output+"\n"
