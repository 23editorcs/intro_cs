# removeDup.py

def main(aList):
    newList = []
    for i in range(len(aList)):
        if aList[i] not in newList:
            newList.append(aList[i])
    return newList
