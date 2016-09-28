# Total Name Numeric
# totalNameNumeric.py

def main():
    # Introduction
    print('The program calculates your numeric full name by ASCII' \
          'case-insensitive.')
    # Get a file name
    infileName = input('Enter the file name: ')
    # Open the file
    infile = open(infileName, 'r')
    outfile = open(infileName, 'a')
    # Read the file line by line
    for line in infile:
        # Get a full name input, upper it.
        name = line
        name = name.upper()
        # Seperate the name into words
        words = name.split()
        # Iterate through every word and convert every letter to number
        # Add up to the number
        number = 0
        for word in words:
            for i in word:
                number = number + ord(i) - 64
        # Rule them all
        print('Your full name numeric is {0}.'.format(number), file = outfile)
    infile.close()
    outfile.close()

main()
