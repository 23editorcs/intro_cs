# Circle Intersection
# intersection.py

# Design Algorithm
    # import graphics, math
    # Print an introduction
    # Get the radius of circle and the line y = a from user
    # Draw a graphics window set it background white
    # Set window to coordinates(-10, -10, 10, 10)
    # Draw a circle at (0, 0) with the radius
    # Draw the line y = a
    # Calculate the intersection by x = +/- sqrt(r^2 - y^2)
    # Change the color of points (x, y), (-x, y)
    # Print the value of 2 points (x, y), (-x, y)
    # Get the user click to close

from graphics import *
import math

def main():
    # Introduction
    print('The program calculates the intersection between circle and line.')

    # Get the radius and y
    r = eval(input('What is the circle\'s radius? '))
    y = eval(input('What is the line y? '))

    # Create a graphics window
    win = GraphWin('Circle Intersection', 400, 400)
    win.setBackground('white')
    win.setCoords(-10, -10, 10, 10)

    # Draw a circle and line
    Circle(Point(0,0), r).draw(win)
    Line(Point(10, y), Point(-10,y)).draw(win)

    # Calculate intersection
    x1 = math.sqrt(r**2 - y**2)
    x2 = -math.sqrt(r**2 - y**2)

    # Draw the Points
    p1 = Point(x1, y)
    p2 = Point(x2, y)
    p1.setOutline('red')
    p2.setOutline('red')
    p1.draw(win)
    p2.draw(win)

    # Draw 2 labels for 2 points
    l1 = Text(Point(x1, y + 0.5), '({0}, {1})'.format(x1, y))
    l2 = Text(Point(x2, y + 0.5), '({0}, {1})'.format(x2, y))
    l1.draw(win)
    l2.draw(win)

    # Click to close
    win.getMouse()
    win.close()

main()
    
