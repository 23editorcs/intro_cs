# Future Value Graphic
# futValGraph.py

from graphics import *

    # Print an introduction
    # Get value of principal and apr from user
    # Create a 320x240 graphic windown titled "Investment Growth Chart"
    # Draw label ' 0.0K' at (20, 230)
    # Draw label '2.5K' at (20, 180)
    # Draw label '5.0K' at (20, 130)
    # Draw label '7.5K' at (20, 80)
    # Draw label '10.0K' at (20, 30)
    # Draw a rectangle from (40, 230) to (65, 230 - principal * 0.02)
    # For year running from a value of 1 up through 10
        # Calculate principal = principal * (1 + apr)
        # Calculate x11 = year * 25 + 40
        # Draw a rectangle from (x11, 230) to (x11 + 25, principal * 0.02)
    # Wait for user press Enter
def main():
    # Introduction
    print('The program calculates and draws a chart of Investment')
    # Get principal and apr value


    # Create a graphic win
    win = GraphWin('Investment Growth Chart', 320, 240)
    win.setBackground('white')

    # Create Entries and Labels
    principalInput = Entry(Point(160, 120), 6)
    aprInput = Entry(Point(160, 140), 6)
    principalLabel = Text(Point(80, 120), 'Your Principal: ')
    aprLabel = Text(Point(80, 140), 'The Apr: ')

    # Draw Entries and Labels
    principalInput.draw(win)
    aprInput.draw(win)
    principalLabel.draw(win)
    aprLabel.draw(win)

    # Undraw Entries and Labels after click
    win.getMouse()   
    principalInput.undraw()
    aprInput.undraw()
    principalLabel.undraw()
    aprLabel.undraw()

    # Get the value principal, apr
    principal = eval(principalInput.getText())
    apr = eval(aprInput.getText()) 

    # Draw left label
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # Draw the 1st principal bar
    Rectangle(Point(40, 230), Point(65, 230 - principal * 0.02)).draw(win)

    # Draw successive bars
    for year in range(1, 11):
        # calculate principal
        principal = principal * (1 + apr)
        # calculate x11
        x11= year * 25 + 40
        # draw a rectangle
        Rectangle(Point(x11, 230), Point(x11 + 25, 230 - principal * 0.02)).draw(win)
    input('Press <Enter> to quit')
    win.close()
main()
    
