# deck.py
# Deck Class

from random import randrange

class Deck:
    """ A Deck object includes 52 standard cards
        organize in order. """
    def __init__(self):
        # Return 52 cards in standard order
        self.cards = self.__createCards()

    def __createCards(self):
        cards = []
        for suit in ['Diamond', 'Club', 'Heart', 'Spade']:
            for rank in range(1,14):
                cards.append((rank, suit))
        return cards

    def shuffle(self):
        # Shuffle all the cards
        for i in range(52):
            card = self.cards[i]
            j = randrange(0,52)
            self.cards.remove(card)
            self.cards.insert(j, card)

    def dealCard(self):
        # Return 1 card on the top
        card = self.cards.pop(0)
        return card

    def cardsLeft(self):
        # Number of cards left
        numCards = len(self.cards)
        return numCards
