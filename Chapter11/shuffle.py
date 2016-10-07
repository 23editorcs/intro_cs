# shuffle.py
# Shuffle a List

from random import randrange

def main(aList):
    for i in range(len(aList)):
        val = aList.pop(i)
        j = randrange(0, len(aList))
        aList.insert(j, val)

    print(aList)
    
