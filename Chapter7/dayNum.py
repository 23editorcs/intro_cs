# Day Num with a Date
# dayNum.py

def main():
    # Introduction
    print('The program calculate the number of days for a date.')
    # Get a Date
    date = input('Enter a date with mm/dd/yyyy format: ')
    # Seperate the date into month, day, year
    m, d, y = map(int, date.split('/'))
    dayNum = 31 * (m -1) + d
    if m > 2:
        dayNum = dayNum - (4 * m + 23) / 10
    if leapYear(y) and m > 2:
        dayNum = dayNum + 1
    print('This date is {0} day of this year.'.format(int(dayNum)))

def leapYear(year):
    # Check a year is a leap year or not
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    main()
