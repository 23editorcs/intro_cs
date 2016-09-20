# Winter Screen
# winter.py

from graphics import *

def main():
    # Instruction
    print('The program draws a winter screen.')
    # Draw a graphics window
    win = GraphWin('Winter Screen', 400, 400)
    win.setBackground('white')
    # Draw a tree
    tree = Rectangle(Point(175, 200), Point(225, 300))
    tree.setFill('green')
    leaves = Rectangle(Point(125, 150), Point(275, 250))
    leaves.setFill('green')
    tree.draw(win)
    leaves.draw(win)
    # Draw a snowman
    
    # Rule them all
    win.getMouse()
    win.close()

main()
