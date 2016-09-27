# Acronym Program
# acronym.py

def main():
    # Introduction
    print('The program returns an Acronym of a phrase.')
    # Get an input phrase
    phrase = input('Type a phrase: ')
    # Split the phrase into words
    words = phrase.split()
    # Get the first letter of each word add to a string
    acronym = ''
    for word in words:
        acronym = acronym + word[0]
    # Upper the acronym
    acronym = acronym.upper()
    # Rule them all
    print('Your Acronym is {0}'.format(acronym))

main()
