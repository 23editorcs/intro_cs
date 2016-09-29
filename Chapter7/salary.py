# Salary Payment
# salary.py

def main():
    # Introduction
    print('The program calculate the total wages for a week.')
    # Get the hours worked, hourly rate
    hours, rate = eval(input('Enter the hours worked and hourly rate:'\
                             '(seperate by comma) '))
    # Put everything in try/except
    try:
        # Create a two-way decision if the hours wokred > 40,
        # then get the over multiple 1.5
        if hours > 40:
            totalWages = 40 * rate + 1.5 * (hours - 40) * rate
        else:
            totalWages = hours * rate
        print('Your total wages this week is {0:.2f}.'.format(totalWages))
    except:
        print('Something is wrong!')

if __name__ == '__main__':
    main()
