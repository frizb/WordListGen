import argparse
from string import maketrans
new_word_list = []
leet_trans = ["aeiotsbzAEIOTSBZ","4310758243107582","altsALTS","@!+$@!+$"]

print('\033[0;32m'+"WordListGen: " + '0.1' + " Updated: " + 'March 22, 2018' +'\033[0;39m')
parser = argparse.ArgumentParser(description='\033[0;31m'+'WordListGen - Very Simple Word List Morpher - Creates a list of unique words for fuzzing / brute forcing'+'\033[0;39m')
parser.add_argument("-all", action='store_true', help='Runs all word list morphers')
parser.add_argument("-lower", action='store_true', help='Lowercase each word on the input list')
parser.add_argument("-upper", action='store_true', help='Uppercase each word on the input list')
parser.add_argument("-leet", action='store_true', help='Uppercase each word on the input list')
parser.add_argument("-swap", action='store_true', help='Swap the case of the word list')
parser.add_argument("-capitalize", action='store_true', help='Capitalize the first letter of the word list')
parser.add_argument("-orig", action='store_true', help='Include the original word from the word list')
parser.add_argument("-min", type=int, default="3", help='Minimum word size (default: %(default)s)')
parser.add_argument("-max", type=int, default="20", help='Maximum word size (default: %(default)s)')
parser.add_argument("-input", metavar='file', type=str, default="wordlist.txt", help='Input wordlist (default: %(default)s)')
parser.add_argument("-output", metavar='file', type=str, default="wordlistout.txt", help='Output wordlist (default: %(default)s)')
args = parser.parse_args()

with open(args.input, "r") as filein:
    for line in filein:
        if ( len(line) < args.min or len(line) > args.max ): continue
        if (args.lower or args.all): new_word_list.append(line.lower())
        if (args.upper or args.all): new_word_list.append(line.upper())
        if (args.leet or args.all): new_word_list.append(line.translate(maketrans(leet_trans[0], leet_trans[1])))
        if (args.leet or args.all): new_word_list.append(line.translate(maketrans(leet_trans[2], leet_trans[3])))
        if (args.leet or args.all): new_word_list.append(line.translate(maketrans(leet_trans[2], leet_trans[3])).translate(maketrans(leet_trans[0], leet_trans[1])))
        if (args.swap or args.all): new_word_list.append(line.swapcase())
        if (args.capitalize or args.all): new_word_list.append(line.title())
        if (args.orig or args.all): new_word_list.append(line)

with open(args.output,"w") as fileout:
    fileout.writelines(sorted(list(set(new_word_list))))
print '\033[0;34m'+"DONE!\n "+'\033[0;33m'+"Wordlist input:\t"+'\033[0;39m'+args.input+"\n"+'\033[0;33m'+" Wordlist output:\t"+'\033[0;39m'+args.output+"\n"
