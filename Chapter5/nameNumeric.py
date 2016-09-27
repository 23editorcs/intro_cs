# Numeric Name
# nameNumeric.py

def main():
    # Introduction
    print('The program returns a numeric value for your name.')
    # Get the name
    name = input('Enter your name: ')
    # Change every character of the name into number
    # Using ASCII code, and start with a = 1, case-insensitive
    number = 0
    name = name.upper()
    for i in name:
        number = number + ord(i) - 64
    # Rule them all
    print('Your Numeric Value is {0}.'.format(number))

main()
