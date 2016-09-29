# Babysitter
# baby.py

def main():
    # Introduction
    print('The program calculates the babysitting wage for a day.')
    # Get the hours and minutes start and end
    startHour, startMin = eval(input('Enter the starting hour and minute: '))
    endHour, endMin = eval(input('Enter the ending hour and minute: '))
    # Calculate with decision tree, if ending hour > 21
    # the rate drops to 1.75, otherwise 2.50

    startHourFull = startHour + startMin / 60
    endHourFull = endHour + endMin / 60
    if startHour < 21 and endHour < 21:
        wage = (endHourFull - startHourFull) * 2.50
    elif startHour < 21 and endHour > 21:
        wage = (21 - startHourFull) * 2.50 + (endHourFull - 21) * 1.75
    else:
        wage = (endHourFull - startHourFull) * 1.75
    print('Your wage from {1} to {2} is {0}.'.format(wage, startHourFull, endHourFull))

if __name__ == '__main__':
    main()
