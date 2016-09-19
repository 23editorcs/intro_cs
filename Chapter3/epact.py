# Epact
# epact.py

def main():
    # Instruction
    print('The program calculates the epact days.')
    # Get the year
    year = eval(input('Give me a year: '))
    # Calculate epact
    c = year // 100
    epact = (8 + (c//4) - c + ((8 * c + 13)//25) + 11 * (year%19))%30
    # Rule them all
    print('The epact days is {0}.'.format(epact))

main()
