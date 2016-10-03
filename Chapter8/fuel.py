# fuel.py
# Fuel Efficience of a Multi-Leg Journey

def main():
    '''
    Input the o starting odometer and n number of legs.
    Save a start odomeper for every leg, os = o
    Loop to n legs:
     Input the c odometer of current leg, g the gas uses in the leg.
     The miles m equals c minus os
     MPG in the leg equals m divide g
     Keep total gas in totalGas equals all of gases
     Update os equals os plus c
     Print out the mpg per leg
    Print out the average mpg, (os - o) / totalGas
    '''
    # Introduction
    print('The program calculates miles per gas in a multi-leg journey.')
    # Get the starting odometer & number of legs.
    o, n = eval(input('Enter the starting odometer, numer of legs (separate by comma):'))
    # Save a start odometer for every leg
    os = o
    totalGas = 0
    # Loop to n legs:
    for i in range(n):
        c, g = eval(input('Enter the current odometer, used gas (separate by comma): '))
        m = c - os
        mpg = m / g
        totalGas += g
        os += m
        print('Your mpg this leg is {}.'.format(mpg))
    print('Your average mpg is {}.'.format((os-o)/totalGas))

if __name__ == '__main__':
    main()
    
