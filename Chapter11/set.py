# set.py

class Set:

    def __init__(self, elements):
        self.elements = elements

    def addElement(self, x):
        self.elements.append(x)

    def deleteElement(self, x):
        self.elements.remove(x)

    def member(self, x):
        if x in self.elements:
            return True
        else: return False

    def intersection(self, set2):
        newSet = []
        for i in self.elements:
            if i in set2:
                newSet.append(i)
        return newSet

    def union(self, set2):
        newSet = self.elements
        for i in set2:
            if not i in newSet:
                newSet.append(i)
        return newSet

    def subtract(self, set2):
        newSet = self.elements
        for i in set2:
            if i in newSet:
                newSet.remove(i)
        return rewSet
    
        
