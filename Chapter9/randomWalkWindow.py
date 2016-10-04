# randomWalkWindow.py
# Draw Random Walk in a Window

from graphics import *
import time
from random import random
import math

def main():
    printIntro()
    n = getInput()
    win = drawWindow()
    simNSteps(win, n)
    win.getMouse()
    win.close()

def printIntro():
    print('This program simulates the n number of steps with Random Walk '\
          'and draw a line that traces the walk.')

def getInput():
    # Returns the n number of steps to walk
    n = int(input('How many steps to walk? '))
    return n

def drawWindow():
    win = GraphWin('Random Walk', 400, 400)
    win.setCoords(0, 0, 100, 100)
    return win

def simNSteps(win, n):
    # Simulates the n number of random walk
    # Draw a line that traces the progress
    x = y = 50
    for i in range(n):
        x1, y1 = simOneStep(x, y)
        Line(Point(x, y), Point(x1, y1)).draw(win)
        x, y = x1, y1
        time.sleep(0.1)

def simOneStep(x, y):
    # Simulates One Walk
    # Return position after walk
    angel = random() * 2 * math.pi
    x1 = x + math.cos(angel)
    y1 = y + math.sin(angel)
    return x1, y1

if __name__ == '__main__':
    start = time.time()
    main()
    print('{:4f}'.format(time.time() - start))
