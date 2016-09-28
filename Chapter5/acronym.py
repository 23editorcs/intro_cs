# Acronym Program
# acronym.py

def main():
    # Introduction
    print('The program returns an Acronym of a phrase.')
    # Get a file name
    infileName = input('Enter the file name: ')
    outfileName = input('Enter the file name to save: ')
    # Open the file
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')
    # Read the file line by line
    for line in infile:
        phrase = line
        # Split the phrase into words
        words = phrase.split()
        # Get the first letter of each word add to a string
        acronym = ''
        for word in words:
            acronym = acronym + word[0]
        # Upper the acronym
        acronym = acronym.upper()
        # Rule them all
        print('Your Acronym is {0}'.format(acronym), file = outfile)
    # Close the file
    infile.close()
    outfile.close()
main()
