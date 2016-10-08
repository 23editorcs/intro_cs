# cardSort.py
# Group cards by suits and sort by rank

def main():
    print('This program sorts a list of cards by rank and suit')
    filename = input('Enter a file name: ')
    listOfCards = sortCards(filename)
    score = checkScore(listOfCards)
    print(score)

def sortCards(filename):
    infile = open(filename, 'r')
    listOfCards = []
    for line in infile:
         rank, suit = line.split()
         listOfCards.append((rank, suit))
    listOfCards.sort()
    listOfCards.sort(key=sortSuit)
    return listOfCards

def sortSuit(aTuple):
    return aTuple[1]

def checkScore(listOfCards):
    # List of card names
    names = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
             'Nine', 'Ten', 'Jack', 'Queen', 'King']
    # Create 2 list, ranks & suits
    ranks = list(int(card[0]) for card in listOfCards)
    ranks.sort()
    suits = list(card[1] for card in listOfCards)
    # Create rank count list, counts = [0]*13
    counts = [0]*13
    print(ranks, suits)
    # Counts in ranks list
    for i in ranks:
        counts[i - 1] += 1
    print(counts)
    # Check suit in 5 cards
    # if they are same suit
    if suits[0] == suits[4]: 
        # check if they are Royal Fulsh, counts[0] = counts[9] = . = counts[12]
        if counts[0] == counts[9] == counts[10] == counts[11] == counts[12]:
            score = 'Royal Flush'
        # or Straight Flush, ranks[4] - ranks[0] = 4
        elif ranks[4] - ranks[0] == 4:
            score = 'Straight Flush'
        # or Flush
        else:
            score = 'Flush'
    # else
    else:
        # check they are Four of a Kind, if 4 in counts
        if 4 in counts:
            score = 'Four of a Kind'
        # or 3 in counts and 2 in counts
        elif 3 in counts and 2 in counts:
            score = 'Full House'
        # or 3 in counts
        elif 3 in counts:
            score = 'Three of a Kind'
        # or count(counts(2)) == 2
        elif counts.count(2) == 2:
            score = 'Two of Pairs'
        # or 2 in counts
        elif 2 in counts:
            score = 'A Pair'
        # or ranks[4] - ranks[0] = 4 or counts[0] = counts[9] = ...= counts[12]
        elif (ranks[4] - ranks[0] == 4) or (
        counts[0] == counts[9] == counts[10] == counts[11] == counts[12]):
            score = 'Straight'
        # else: ranks[4]
        else: score = names[ranks[4] - 1] + ' Hight'
    return score
        
if __name__ == '__main__': main()
