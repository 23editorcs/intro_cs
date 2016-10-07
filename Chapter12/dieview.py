# dieview.py
# Die View Button

from graphics import *

class DieView:
    """ Die View is a widget that displays a graphical representation of
    a standard six-sided die."""

    def __init__(self, win, center, size):
        """ Creates a view of die, e.g.:
            d1 = DieView(win, Point(50, 50), 20)
            creates a die centered at (50, 50) having sides of length 20."""
        # first defines some standard values
        self.win = win
        self.background = 'white' # color of die face
        self.foreground = 'black' # color of the pips
        self.psize = 0.1 * size
        hsize = size / 2.0
        offset = 0.6 * hsize

        # Create a square for the size
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [
                self.__makePip(cx + offset, cy + offset),
                self.__makePip(cx + offset, cy),
                self.__makePip(cx + offset, cy - offset),
                self.__makePip(cx, cy),
                self.__makePip(cx - offset, cy + offset),
                self.__makePip(cx - offset, cy),
                self.__makePip(cx - offset, cy - offset)
                ]
                
        # Draw an initial value
        self.setValue(1)
        
        # private method to create pip
    def __makePip(self, x, y):
        # Make pip
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        self.value = value
        for i in range(len(self.pips)):
            self.pips[i].setFill(self.background)
            
        valueList = [[], [4], [1,7], [1,4,7], [1,3,5,7], [1,3,4,5,7], [1,2,3,5,6,7]]
        for i in valueList[value]:
            self.pips[i-1].setFill(self.foreground)

    def changeColor(self, color):
        self.foreground = color
        self.setValue(self.value)
        
