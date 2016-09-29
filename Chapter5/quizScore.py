# Quiz Score
# quizScore.py

# import graphics
# Get a file name
# Create a list has 11 int elements equals to 0 for storing the occurence of quiz score
# Check scores in the file line by line
# Use a score as an index to add up the list
# list[score] += 1

from graphics import *

def main():
    # Introduction
    print('The program draws a plot with quiz scores from a file.')
    # Get an infileName
    infileName = input('Enter the file name: ')
    # Open the file
    infile = open(infileName, 'r')
    # Create a list of 11 int elements equal to 0
    scores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Read through the file line by line
    for line in infile:
        # Convert the value to int
        score = eval(line)
        # Use the score as index to add up
        scores[score] += 1
    # Draw a graph window
    win = GraphWin('Quiz Score Plot', 400, 400)
    # Set the coordinates
    win.setCoords(0, 0, 12, max(scores) + 3)
    for i in range(1, max(scores) +3, 1):
        Line(Point(0, i + 0.5), Point(12, i + 0.5)).draw(win)
    # Draw the score from 0-10
    for i in range(11):
        scoreLabel = Text(Point(i + 1, 1), i)
        score = scores[i]
        scorePlot = Rectangle(Point(i + 1, 1.5), Point(i + 1.1, 1.5 + score))
        scoreLabel.draw(win)
        scorePlot.draw(win)
    win.getMouse()
    win.close()
    infile.close()
main()
