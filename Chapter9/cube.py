# cube.py
# Advance Exercise

from random import random

def main():
    printIntro()
    n = getInput()
    fraction = simNLook(n)
    printOutput(fraction)

def printIntro():
    print('This program simulates the Monte Carlo inside a cube '\
          'return the probability to look at one side in the cube.')

def getInput():
    # Return the n number to look
    n = int(input('How many times to look? '))
    return n

def simNLook(n):
    # Simulates the n number of look inside a cube
    # Return a fraction that look at one side
    count = 0
    for i in range(n):
        pos = simOneLook()
        if pos:
            count += 1
    fraction = count / n
    return fraction

def simOneLook():
    # Simulates One Look with a position at x = 1/2, y = 0, z = 0
    # Return True if the look see the (1, y, z), otherwise False
    # When move x to 1/2 near the (1, y, z), calculate the slope from
    #  (1/2, 0, 0) to 4 edges (1, 1, z), (1, -1, z), (1, y, 1), (1, y, -1)
    #   slope xy = (y1 - y) / (x1 - x) = [-2, 2]
    #   slope xz = [-2, 2]
    #   x > 1/2
    # x from -1/2, 3/2 because it moves 1/2
    x = random() * 2 - 0.5
    y = random() * 2 - 1.0
    z = random() * 2 - 1.0
    xy = y / (x - 1/2)
    xz = z / (x - 1/2)
    if x > 1/2:
        if -2 <= xy <= 2 and -2 <= xz <= 2:
            return True
        else: return False

def printOutput(fraction):
    print('The fraction of look at (1,y,z) is {:.2%}.'.format(fraction))
    
if __name__ == '__main__':
    main()
