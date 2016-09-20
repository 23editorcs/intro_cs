# Line Segment Information
# line.py

# Design Algorithm
    # import graphics, math
    # Print an introduction
    # Draw a graphics window
    # Get 2 clicks from user
    # Get the midpoint, draw with cyan
    # Draw the line
    # Calculate the length, slope by formula
        # slope = dy / dx
        # length = sqrt(dy^2 + dx^2)
    # Print them out
    # Get a click to close

import math
from graphics import *

def main():
    # Introduction
    print('The program returns Line Segment Information.')

    # Draw a graphics window
    win = GraphWin('Line Segment Information', 400, 400)
    win.setBackground('white')

    # Get 2 click from user
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Draw a line
    l = Line(p1, p2)
    l.draw(win)
    
    # Get the midpoint, draw with cyan
    m = l.getCenter()
    m.setOutline('cyan')
    m.draw(win)

    # Calculate the slope, length
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    slope = dy / dx
    length = math.sqrt(dx ** 2 + dy ** 2)

    #Print the slope, length
    label = Text(Point(200, 380), 'The slope is {0:.2f}, and the length is'\
                 '{1:.2f}.'.format(slope, length))
    label.draw(win)

    # Click to close
    win.getMouse()
    win.close()

main()
    
