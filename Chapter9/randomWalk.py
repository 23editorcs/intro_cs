# randomWalk.py
# Random Walk Simulation

from random import random
import time

def main():
    printIntro()
    n = getInput()
    steps = simNWalks(n)
    printOutput(steps, n)

def printIntro():
    print('This program simulates the Random Walk one-dimensional '\
          'and returns the steps you ahead or behind starting point.')

def getInput():
    # Returns the n number of times to walk
    n = int(input('How many times to walk? '))
    return n

def simNWalks(n):
    # Return the steps after n walks
    steps = 0
    for i in range(n):
        step = simOneWalk()
        steps += step
    return steps

def simOneWalk():
    # Simulates One walk
    # Return 1 or -1
    if random() < 0.5:
        step = 1
    else:
        step = -1
    return step

def printOutput(steps, n):
    print('After {0} walks, you are {1} away from the starting point.'\
          .format(n, steps))

if __name__ == '__main__':
   startTime = time.time()
   main()
   print('{:.4f}'.format(time.time() - startTime))
