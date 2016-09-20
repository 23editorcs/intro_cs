# Archery Target
# archery.py

from graphics import *

def main():
    # Instruction
    print('The program draws a archery target.')
    # Draw a graphics window
    win = GraphWin('Archery Window', 400, 400)
    # Draw the circle from out to inside
    blue = Circle(Point(200, 200), 100)
    blue.setFill('blue')

    red = Circle(Point(200, 200), 75)
    red.setFill('red')

    green = Circle(Point(200, 200), 50)
    green.setFill('green')

    yellow = Circle(Point(200, 200), 25)
    yellow.setFill('yellow')

    blue.draw(win)
    red.draw(win)
    green.draw(win)
    yellow.draw(win)
    # Print Text to close
    text = Text(Point(200, 350), 'Click to close')
    text.draw(win)
    # Rule them all
    win.getMouse()
    win.close()

main()
