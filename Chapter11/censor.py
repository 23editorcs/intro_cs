# censor.py

import re

def main():
    print('This program returns a text file with censor all 4-letter-words')
    filename = input('Enter a file name: ')
    censoredFile = input('Enter a file name that stores censored words: ')
    strings = toCensor(filename, censoredFile)
    print(strings)

def toCensor(filename, censoredFile):
    infile = open(filename, 'r', encoding='utf-8')
    censorFile = open(censoredFile, 'r', encoding='utf-8')
    text = infile.readline()
    words = censorFile.readline()
    listText = re.split('(\W+)', text)
    print(listText)
    listWords = re.split('\W+', words)
    for i in range(len(listText)):
        if listText[i] in listWords:
            listText[i] = '*'*len(listText[i])
    strings = ''.join(listText)
    return strings
    
if __name__ == '__main__': main()
