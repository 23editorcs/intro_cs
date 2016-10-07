# gpasort.py

from graphics import *
from gpa import Student, makeStudent
from button import Button

def main():
    win = GraphWin('Students Sort', 400, 400)
    win.setCoords(0, 0, 4, 5)
    input1, input2, bList = drawInterface(win)
    while True:
        p = win.getMouse()
        for b in bList:
            if b.clicked(p):
                label = b.getLabel()
                if label != 'Quit':
                    students = readStudents(input1.getText())
                    listOfTuples = toTuples(students)
                    listOfTuples.sort()
                    students = toStudents(listOfTuples)
                    writeStudents(students, input2.getText())
                    Text(Point(2, 2.5), 'Done').draw(win)
                else:
                    win.close()

def toStudents(listOfTuples):
    students = []
    for t in listOfTuples:
        students.append(t[1])
    print(students)
    return students

def toTuples(students):
    # Return a list of tuples with Student object and GPA value
    listOfTuples = []
    for s in students:
        t = (s.gpa(), s)
        listOfTuples.append(t)
    return listOfTuples
    

def drawInterface(win):
    text1 = Text(Point(1,4), 'Enter the data file name: ')
    text2 = Text(Point(1,2), 'Enter a file name to write: ')
    input1 = Entry(Point(1,3), 20)
    input2 = Entry(Point(1,1), 20)
    text1.draw(win)
    text2.draw(win)
    input1.draw(win)
    input2.draw(win)
    bList = createButtons(win)
    return input1, input2, bList

def createButtons(win):
    bNames = ['Quit', 'Name Sort', 'Credits Sort', 'GPA Sort']
    bList = []
    for i in range(4):
        b = Button(win, Point(3, i+1), .75, .5, bNames[i])
        b.activate()
        bList.append(b)
    return bList

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def keySort(key):
    if key == 'Name Sort':
        return Student.getName
    elif key == 'Credits Sort':
        return Student.getQPoints
    elif key == 'GPA Sort':
        return Student.gpa
    else: return 'None'
    
def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print('{0}\t{1}\t{2}'.format(s.getName(), s.getHours(), s.getQPoints()),
              file=outfile)
    outfile.close()
    
if __name__ == '__main__': main()
