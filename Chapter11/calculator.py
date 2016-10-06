# calculator.py
# Calculator Interface

from button import Button
from graphics import *

class Calculator:
    def __init__(self):
        # Create the window for the calculator
        win = GraphWin('Calculator')
        win.setCoords(0, 0, 6, 7)
        win.setBackground('slategray')
        self.win = win
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        # create a list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'), (5,4,'C')
                  ]
        self.buttons = []
        for (cx, cy, label) in bSpecs:
            self.buttons.append(Button(self.win, Point(cx,cy), .75, .75, label))
            
        # create the larger '=' button
        self.buttons.append(Button(self.win, Point(4.5,1),
                                   1.75, .75, '='))
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __createDisplay(self):
        # calculator display
        bg = Rectangle(Point(.5, 5.5), Point(5.5, 6.5))
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(3,6), '')
        text.draw(self.win)
        text.setFace('courier')
        text.setStyle('bold')
        text.setSize(16)
        self.display = text

    def run(self):
        # Infinite 'event loop' to process button clicks
        while True:
            key = self.getKeyPress()
            self.processKey(key)

    def getKeyPress(self):
        # Waits for a button to be clicked
        # Returns the label of the button that was clicked
        while True:
            # loop for each mouse click
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel() # method exit

    def processKey(self, key):
        # Updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == 'C':
            self.display.setText('')
        elif key == '<-':
            # Backspace, slice off the last character
            self.display.setText(text[:-1])
        elif key == '=':
            # Evaluate the expression and display the result
            # the try...except mechanism "catches" errors in the
            # formula being evaluated
            try:
                result = eval(text)
            except:
                result = 'ERROR'
            self.display.setText(str(result))
        else:
            # Normal key press, append it to the end of display
            self.display.setText(text+key)

if __name__ == '__main__':
    theCal = Calculator()
    theCal.run()
    
