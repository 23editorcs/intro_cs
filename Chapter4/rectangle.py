# Rectangle Segment Information
# rectangle.py

# Design Algorithm
    # Import graphics, math
    # Print an introduction
    # Create a graphics window
    # Get two clicks from user
    # Draw a rectangle with 2 points
    # Calculate length and width
    # Calculate perimeter, area by formula
        # perimeter = 2 * (width + length)
        # area = width * length
    # Print them out
    # Click to close

import math
from graphics import *

def main():
    # Introduction
    print('The program returns Rectangle Segment Information.')

    # Create a graphics window
    win = GraphWin('Rectangle Segment Information', 400, 400)
    
    # Get 2 clicks from user
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Draw a rectangle
    Rectangle(p1, p2).draw(win)

    # Calculate length, width
    width = abs(p2.getX() - p1.getX())
    length = abs(p2.getY()- p1.getY())

    # Calculate perimeter, area
    perimeter = 2 * (width + length)
    area = width * length

    # Print them out
    label = Text(Point(200, 380), 'The perimeter is {0:.2f}, and area is'\
                 ' {1:.2f}.'.format(perimeter, area))
    label.draw(win)

    # Click to close
    win.getMouse()
    win.close()

main()
