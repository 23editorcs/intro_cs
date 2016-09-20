# House with five-click
# house.py

# Design Algorithm
    # Import graphics
    # Print an introduction
    # Create a graphics window
    # Get 2 clicks
    # Draw the house
    # Get click 3
    # Calculate 2 points of the door (p31, p32)
        # The door width = 1/5 * (x2 - x1), x31 = x3 - 1/2 * width, y32 = y3
        # x32 = x3 + 1/2 * width, y32 = y1
        # (x31, y3), (x32, y1)
    # Draw the door with Rectangle
    # Get the click 4
    # Calculate 2 points of the window p41, p42
        # x41 = x4 - 1/4 * width, y41 = y4 - 1/4 * width
        # x42 = x4 + 1/4 * width, y42 = y4 + 1/4 * width
    # Draw the windoor
    # Get the click 5
    # Draw a Polygon with p5, p2, (x1, y2)
    # Click to close

from graphics import *

def main():
    # Introduction
    print('The program draws a house with 5 clicks.')

    # Create a graphics window
    win = GraphWin('The House', 400, 400)
    win.setBackground('white')

    # Get 2 clicks
    p1 = win.getMouse()
    p2 = win.getMouse()

    # Draw the wall
    Rectangle(p1,p2).draw(win)

    # Get the click 3
    p3 = win.getMouse()

    # Calculate 2 points of the door
    width = 1/5 * (p2.getX() - p1.getX())
    x31 = p3.getX() - 1/2 * width
    x32 = p3.getX() + 1/2 * width

    # Draw the door
    Rectangle(Point(x31, p3.getY()), Point(x32, p1.getY())).draw(win)

    # Get the click 4
    p4 = win.getMouse()

    # Calculate 2 points of the window
    x41 = p4.getX() - 1/4 * width
    y41 = p4.getY() - 1/4 * width
    x42 = p4.getX() + 1/4 * width
    y42 = p4.getY() + 1/4 * width

    # Draw the window
    Rectangle(Point(x41, y41), Point(x42, y42)).draw(win)

    # Get the click 5
    p5 = win.getMouse()

    # Draw a Polygon
    Polygon(p5, p2, Point(p1.getX(), p2.getY())).draw(win)

    # Click to close
    win.getMouse()
    win.close()

main()
