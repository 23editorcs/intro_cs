# average4.oy

def main():
    sums = 0.0
    count = 0
    xStr = input('Enter a number (<Enter> to quit) >> ')
    while xStr != '':
        x = eval(xStr)
        sums += x
        count += 1
        xStr = input('Enter a number (<Enter> to quit) >> ')
    print('\nThe average of the numbers is', sums / count)

main()
