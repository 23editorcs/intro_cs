# cbutton.py
# Circular Button Class

from graphics import *
from math import sqrt

class CButton:
    """ A Button is a labeleb circular in a window. It is created with center,
    radius, label. It is activated or deactivated with the active() and
    deactive() methods. The clicked() method return True if the button is active
    and the click is inside it."""
    def __init__(self, win, center, radius, label):
        self.win = win
        self.x = center.getX()
        self.y = center.getY()
        self.radius = float(radius)
        self.label = Text(center, label)
        self.cir = Circle(center, radius)
        self.cir.setFill('lightgray')

        self.active()
        self.cir.draw(win)
        self.label.draw(win)

    def getLabel(self):
        return self.label.getText()

    def getCenter(self):
        return self.cir.getCenter()

    def getRadius(self):
        return self.radius

    def active(self):
        self.active = True
        self.label.setFill('black')
        self.cir.setWidth(2)

    def deactive(self):
        self.active = False
        self.label.setFill('lightgray')
        self.cir.setWidth(1)

    def clicked(self, p):
        px, py = p.getX(), p.getY()
        dx = sqrt((px - self.x)**2 + (py - self.y)**2)
        return self.active and dx <= self.radius

def main():
    win = GraphWin()
    b = CButton(win, Point(50, 50), 10, 'Tron')
    while True:
        p = win.getMouse()
        if b.clicked(p):
            win.close()

if __name__ == '__main__':
    main()
        
        
