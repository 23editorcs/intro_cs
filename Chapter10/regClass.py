# regClass.py
# An Object of Regression

class Regression:
    """ A Regression is an object that stores values of regression formula.
        Add a point to it with addPoint() method.
        Predict an y value with predict() method. """
    def __init__(self, x = 0, y = 0, x2 = 0, xy = 0, n = 0):
        # Input inital value of regression formula
        self.x = x
        self.y = y
        self.x2 = x2
        self.xy = xy
        self.n = n

    def addPoint(self, p):
        # Add a point to object
        px = p.getX()
        py = p.getY()
        # Increase values of the object
        self.x += px
        self.y += py
        self.x2 += px ** 2
        self.xy += px * py
        self.n += 1
        self.meanx = self.x / self.n
        self.meany = self.y / self.n

    def predict(self, x):
        # Predict the value y with x
        return (self.meany + self._m() * (x - self.meanx))
    def _m(self):
        return ((self.xy - self.n * self.meanx * self.meany) /
                (self.x2 - self.n * (self.meanx ** 2)))
