# statSet.py

from math import sqrt

class StatSet:
    """ A Stat Set object is used to do simple statistical calculations"""
    def __init__(self):
        self.listX = []


    def addNumber(self, x):
        # Add x to Object
        self.listX.append(x)

    def mean(self):
        # Return the mean of Object
        sums = 0
        for i in self.listX:
            sums += i
        return sums / len(self.listX)

    def median(self):
        # Return the median of Object
        size = len(self.listX)
        self.sortList = self.listX
        self.sortList.sort()
        midNum = size // 2 
        if size % 2 == 0:
            median = (self.sortList[midNum] + self.sortList[midNum - 1]) / 2.0
        else:
            median = self.sortList[midNum]
        return median

    
    def stdDev(self):
        xbar = self.mean()
        size = len(self.listX)
        sumDevSq = 0.0
        for num in self.listX:
            dev = num - xbar
            sumDevSq += dev * dev
        return sqrt(sumDevSq / (size - 1))

    def count(self):
        counts = 0
        for num in self.listX:
            counts += 1
        return counts

    def min(self):
        return self.sortList[0]

    def max(self):
        return self.sortList[-1]
