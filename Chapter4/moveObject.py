# Moving Object
# moveObject.py
from graphics import *

def circle():
    # Instruction
    print('The program moves objects around follow the click.')
    # Draw a circle
    win = GraphWin('Circle Moving', 400, 400)
    circle = Circle(Point(200, 200), 25)
    circle.setOutline('purple')
    circle.setFill('red')
    circle.draw(win)
    # Make it move with click
    for i in range(10):
        p = win.getMouse()
        c = circle.getCenter()
        circle.move((p.getX() - c.getX()), (p.getY() - c.getY()))
    # Rule them all
    win.close()

def square():
    # Instruction
    print('The program creates square after a click.')
    # Draw win and a square
    win = GraphWin('Square Clone', 400, 400)
    shape = Rectangle(Point(50,50), Point(70, 70))
    shape.setOutline('red')
    shape.setFill('purple')
    shape.draw(win)
    # Make it clone
    for i in range(3):
        p = win.getMouse()
        clone = shape.clone()
        c = clone.getCenter()
        clone.move((p.getX() - c.getX()), (p.getY() - c.getY()))
        clone.draw(win)
    # Print close Text
    text = Text(Point(200, 350), 'Click to close')
    text.draw(win)
    win.getMouse()
    # Rule them all
    win.close()
    
square()
    
