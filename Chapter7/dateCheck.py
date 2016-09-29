# Date Checker
# dateCheck.py

def main():
    # Introduction
    print('The program checks a date is valid or invalid.')
    # Get a date with format month/day/year
    date = input('Enter a date with month/day/year format: ')
    # Seperate the date
    month, day, year = map(int, date.split('/'))
    print(month, day, year)
    # Check the leap year or not
    if leapYear(year):
        if month == 2:
            if day > 29:
                print('Invalid')
            else:
                print('Valid')
        else:
            checkMonth(month, day)
    else:
        checkMonth(month, day)

def leapYear(year):
    # Check a year is a leap year or not
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def checkMonth(month, day):
    # Check the day is valid with the month
    # 1,3,5,7,9,11 have 30 day
    # 4,6,8,10 have 31 day
    # 2 has 28 day
    if month == 2:
        if day <= 28:
            print('Valid')
        else:
            print('Invalid')
    elif month % 2 == 0:
        if month >= 8:
            if day <= 31:
                print('Valid')
            else:
                print('Invalid')
        else:
            if day <= 30:
                print('Valid')
            else:
                print('Invaid')            
    else:
        if month > 7:
            if day <= 30:
                print('Valid')
            else:
                print('Invaid')
        else:
            if day <= 31:
                print('Valid')
            else:
                print('Invalid')

if __name__ == '__main__':
    main()
            
