#!/usr/bin/python3 -W all
"""
    tokenize.py: tokenize tweet text: return one line per line
    usage: tokenize.py < file
    20171123 erikt(at)xs4all.nl
"""

import nltk
import sys

def tokenize(text):
    tokenizedList = nltk.word_tokenize(text)
    tokenizedLine = ""
    for i in range(0,len(tokenizedList)):
        if i == 0: tokenizedLine = tokenizedList[i]
        else: tokenizedLine += " "+tokenizedList[i]
    return(tokenizedLine)

def main(argv):
    for line in sys.stdin:
        tokenizedLine = tokenize(line)
        print(tokenizedLine)
    sys.exit(0)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
