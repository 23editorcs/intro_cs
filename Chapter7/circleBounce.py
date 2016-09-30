# Circle Bouncing
# circleBounce.py

# Draw a circle (p, r) anywhere in the interior of the window (X, Y)
# Move it around with dx, dy = 1
# If it hits the edge of x change dx = -1, the edge of y change dy = -1
#   xp' + r = X => dx = 1; xp' - r = 0 => dx = 1

from graphics import *
from time import sleep

def main():
    # Introduction
    print('The program move a circle around a window, bouncing against the edge')
    # Draw a graphics window
    win = GraphWin('Bouncing Circle', 400, 400)
    win.setCoords(0, 0, 100, 100)
    # Draw an initial circle with p, r
    circle = Circle(Point(11, 75), 10)
    circle.setFill('purple')
    circle.draw(win)
    # Iterate 10000 times to move it around
    dx, dy = 1, 1
    for i in range(1000):
        circle.move(dx, dy)
        p = circle.getCenter()
        x, y = p.getX(), p.getY()
        if dx == 1 and x + 10 == 100:
            dx = -1
        if dx == -1 and x - 10 == 0:
            dx = 1
        if dy == 1 and y + 10 == 100:
            dy = -1
        if dy == -1 and y - 10 == 0:
            dy = 1
        sleep(0.005)

if __name__ == '__main__':
    main()
