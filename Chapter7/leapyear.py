# Leap Year
# leapyear.py

def main():
    # Introduction
    print('The program calculate a year is leap year or not.')
    # Get a year
    y = int(input('Enter a year: '))
    # Check leap year:
    if y % 4 == 0:
        if y % 100 == 0 and y % 400 != 0:
            print('{0} is not a leap year.'.format(y))
        else:
            print('{0} is a leap year.'.format(y))
    else:
        print('{0] is not a leap year.'.format(y))

if __name__ == '__main__':
    main()
    
