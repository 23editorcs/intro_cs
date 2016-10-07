# wordfreq.py
# Words Frequency

""" Counting frequency of each words in a file"""
import re

def main():
    print('The program counts the frequency of each words '\
          'in a file, and returns a top 10 words and counts.')
    filename = input('Enter the file name: ')
    counts = countWords(filename)
    listSorted = wordsSort(counts)
    printOutput(listSorted)

def countWords(filename):
    # Counts the frequency
    infile = open(filename, 'r')
    # create a dictionary to store pair (word:count)
    counts = {}
    text = infile.read().lower()
    pattern = re.compile('[\W_]+')
    text = pattern.sub(' ', text)
    for w in text.split():
        counts[w] = counts.get(w, 0) + 1
    return counts

def wordsSort(counts):
    # Sort the dictionary by the frequency
    # Create a list stores the tuple with pair word:count
    listSorted = list(counts.items())
    # Alphabet sorted
    listSorted.sort()
    # Frequency Sort byFreq() method
    listSorted.sort(key=byFreq, reverse = True)
    return listSorted

def printOutput(listSorted):
    n = eval(input('How many words to print: '))
    for i in range(n):
        word, count = listSorted[i]
        print('{0:<15}{1:>5}'.format(word,count))

def byFreq(pair):
    return pair[1]

if __name__ == '__main__':
    main()

