# Plotting Student Exam Scores
# plotScore.py

# Import graphics 
# Get a file input, the first line is a total number of students
# The remain lines include the last name and the score, seperate by space
# Draw a graph window, set coordinates follow the number of students
# setCoord(0, 0, n, 130); 100 for the plot, 20 for the names
# Draw the last name at (5, y) left adjust ljust(8), the score (20, y)

from graphics import *

def main():
    # Introduction
    print('The program plots the student\'s scores from a file.')
    # Get an infileName
    infileName = input('Enter the file name: ')
    # Open the file
    infile = open(infileName, 'r')
    # Draw a graph window
    win = GraphWin('The Student\' Scores', 400, 400)
    # Set a coordinate
    # Get the first line of the file
    n = eval(infile.readline())
    win.setCoords(0, 0, 130, n + 1)
    for i in range(0, 130, 10):
        Line(Point(i, 0), Point(i, n+1)).draw(win)
    # Iterate through the lines
    y = 1
    for line in infile.readlines():
        lastName = line.split()[0]
        lastName = '{0:<8}'.format(lastName)
        print(lastName)
        score = eval(line.split()[1])
        nameLabel = Text(Point(10, y), lastName)
        scorePlot = Rectangle(Point(20, y), Point(20 + score, y + 0.2))
        nameLabel.draw(win)
        scorePlot.draw(win)
        y += 1
    win.getMouse()
    win.close()
    infile.close()

main()
