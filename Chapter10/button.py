# button.py
# Button Class definition

from graphics import *

class Button:
    """A Button is a labeled rectangle in a window. It is activated
    or deactivated with the active() and deactive() methods.
    The clicked(p) method returns true if the button is active and
    p is inside it."""

    def __init__(self, win, center, width, height, label):
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmax, self.ymax)
        p2 = Point(self.xmin, self.ymin)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.active()
        self.isChoose = False

    def getLabel(self):
        return self.label

    def active(self):
        # Sets the button to active
        self.active = True
        self.label.setFill('black')
        self.rect.setWidth(2)

    def deactive(self):
        # Sets the button to deactive
        self.active = False
        self.label.setFill('lightgray')
        self.rect.setWidth(1)

    def clicked(self, p):
        # Returns True if button is active and p is inside
        return self.active and (
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)

    def choose(self):
        self.isChoose = True
            
        
        
