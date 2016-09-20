# Triangle Segment Information
# triangle.py

# Design Algorithm
    # Import graphics, math
    # Print an introduction
    # Create a graphics window
    # Get 3 clicks
    # Draw a Polygon with 3 points
    # Calculate a, b, c, 3 lengths of 3 side
        # a = length p1 & p2 = sqrt(dx^2 + dy^2)
        # b = length p1 & p3
        # c = lengh p2 & p3
    # Calculate perimeter, area
    # Show them on the window
    # Click to close

import math
from graphics import *

def main():
    # Introduction
    print('The program returns information of a triangle.')

    # Create a graphics window
    win = GraphWin('Triangle Segment Information', 400, 400)
    win.setBackground('white')

    # Get 3 clicks
    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    # Draw a polygon
    Polygon(p1, p2, p3).draw(win)

    # Calculate a, b, c
    # a = length(p1, p2)
    dxa = p2.getX() - p1.getX()
    dya = p2.getY() - p1.getY()
    a = math.sqrt(dxa ** 2 + dya ** 2)
    # b = length(p1, p3)
    dxb = p3.getX() - p1.getX()
    dyb = p3.getY() - p1.getY()
    b = math.sqrt(dxb ** 2 + dyb ** 2)
    # c = length(p2, p3)
    dxc = p3.getX() - p2.getX()
    dyc = p3.getY() - p2.getY()
    c = math.sqrt(dxc ** 2 + dyc ** 2)

    # Calculate perimeter, area
    perimeter = a + b + c
    s = perimeter / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    # Rule them all
    label = Text(Point(200, 380), 'The perimeter is {0:.2f} and the area is '\
                 '{1:.2f}.'.format(perimeter, area))
    label.draw(win)
    
    # Click to close
    win.getMouse()
    win.close()

main()
