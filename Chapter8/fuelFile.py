# fuelFile.py
# Fuel File Version

def main():
    # Get the file name
    infilename = input('Enter the file name: ')
    # Open the file, reading
    infile = open(infilename, 'r')
    # Read the first line to get starting odometer and number of legs
    
    line = infile.readline().split(' ')
    o = eval(line[0])
    os = o
    totalGas = 0
    # Loop through all the lines
    for line in infile:
        c, g = map(eval, line.split())
        m = c - os
        mpg = m / g
        os += m
        totalGas += g
        print('Your mpg in this leg is {}.'.format(mpg))
    print('Your average mpg is {}.'.format((os - o)/ totalGas))

if __name__ == '__main__':
    main()
    
