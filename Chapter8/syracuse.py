# syracuse.py
# Return a sequence of Syracuse number

def main():
    # Introduction
    print('The program returns a sequence of Syracuse number from the first input.')
    # Get the input
    x = int(input('Enter your number: '))
    # Loop until it comes to 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        print(x, end=', ')

if __name__ == '__main__':
    main()
    
        
