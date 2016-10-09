# sidewalk.py

from random import randrange

def main():
    print('This program simulates random walk inside a side walk')
    n = int(input('How long is the side walk? '))
    squares = [0]*n
    results = doTheWalk(squares)
    print(squares)

def doTheWalk(squares):
    # Random walk inside the Sidewalk
    n = len(squares)
    pos = n // 2
    while pos >= 0 and pos < n:
        squares[pos] += 1
        x = randrange(-1,2,2)
        pos += x
    return squares
    
if __name__ == '__main__': main()
