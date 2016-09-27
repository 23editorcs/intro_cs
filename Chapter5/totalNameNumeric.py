# Total Name Numeric
# totalNameNumeric.py

def main():
    # Introduction
    print('The program calculates your numeric full name by ASCII' \
          'case-insensitive.')
    # Get a full name input, upper it.
    name = input('Enter your full name: ')
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
    print('Your full name numeric is {0}.'.format(number))

main()
