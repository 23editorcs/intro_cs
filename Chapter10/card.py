# card.py
# Black Jack Card

from graphics import *

class Card:
    """ A Card is in black jack include rank and suit.
        Return the rand and suit with getRank and getSuit methods.
        Return Black Jack value with getBJValue method."""
    def __init__(self, rank, suit):
        rankList = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six',
                    'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
        suitList = ['Diamonds', 'Clubs', 'Hearts', 'Spades']
        suitLetter = ['d', 'c', 'h', 's']
        self.BJValue = int(rank)
        self.rank = rankList[rank - 1]
        self.suit = suitList[suitLetter.index(suit)]
        self.filename = 'cards/{0}_of_{1}.gif'.format(self.rank.lower(),self.suit.lower()) 
        

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def getBJValue(self):
        return self.BJValue

    def draw(self, win, center):
        self.display = Image(center, self.filename)
        self.display.draw(win)
        

    def __str__(self):
        return '{0} of {1}'.format(self.rank, self.suit)

def main():
    win = GraphWin('Cards', 500, 500)
    rank = int(input('Enter a rank: '))
    suit = input('Enter the first letter of suit: ')
    c = Card(rank, suit)
    c.draw(win, Point(200,200))
    
if __name__ == '__main__':
    main()
