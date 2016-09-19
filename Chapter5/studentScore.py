# Draw Student Scores Bar
# studentScore.py
from graphics import *

def main():
    # Instruction
    print('The program draws the bar chart with Student Name and')
    print('Score in horizontal.')
    # Get Input from a file
    fileName = input('Give the file name: ')
    inFile = open(fileName, 'r')
    # First line is a total number of student
    total = 0
    total = eval(inFile.readline())
    # Draw a window, set coordinates with 150 horizontal, total + 2 vertical
    win = GraphWin('Student\'s Scores', 400, 400)
    win.setCoords(0, 0, 150, total+2)
    # Sequence lines is LastName Score(0-100) format
    y = 1
    for line in inFile:
        # Separate lastName and score
        lastName = line.split()[0]
        score = eval(line.split()[1])
        # Draw the lastName from bottom up
        # Stat at Point(10, 1), each student increase in vertical by 1
        x = 10
        name = Text(Point(x, y + 0.1), lastName)
        name._reconfig('justify', 'left')
        name.draw(win)
        # Draw the score by a Rectangle with (40, 1) (40 + score, 2)
        bar = Rectangle(Point(40, y), Point(40 + score, y + 0.2)).draw(win)
        bar.setFill('blue')
        y += 1
    # Rule them all
    win.getMouse()
    win.close()

main()
