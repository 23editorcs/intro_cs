# Easter Calculation
# easter.py

def main():
    # Introduction
    print('The program calculates the Easter date in year.')
    # Get a year input
    y = int(input('Enter a year: '))
    # Check the year is in range 1900-2099
    if not 1900 <= y <= 2099:
        print('The year is out the capable.')
        return 0        
    a = y % 19
    b = y % 4
    c = y % 7
    d = (19 * a + 24) % 30
    e = (2 * b + 4 * c + 6 * d + 5) % 7
    easter = 22 + d + e
    # Check the year is in case [1954m 1981, 2049, 2076]
    if y in [1954, 1981, 2049, 2076]:
        easter = easter + 7
        if easter > 30:
            easter = easter - 30
            print('The Easter Day in this year is April {0}.'.format(easter))
        else:
            print('The Easter Day is this year is March {0}.'.format(easter))
    else:
        if easter > 30:
            easter = easter - 30
            print('The Easter Day in this year is April {0}.'.format(easter))
        else:
            print('The Easter Day is this year is March {0}.'.format(easter))

if __name__ == '__main__':
    main()
    
