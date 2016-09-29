# WC program. What the fuck???
# wc.py

def main():
    # Introduction
    print('The super power wc program, not for pop, but for counting.')
    # Get a infileName
    infileName = input('Enter the file name: ')
    # Open the file
    infile = open(infileName, 'r')
    # Set up the variables for hold values
    lineCount, wordCount, charCount = 0, 0, 0
    # Iterate and count everything
    for line in infile:
        lineCount += 1
        lines = line.split()
        for word in lines:
            wordCount += 1
            for i in word:
                charCount += 1
    # Rule them all
    print('Your file has {0} lines, {1} words, {2} characters.'\
          .format(lineCount, wordCount, charCount))
    infile.close()
main()
