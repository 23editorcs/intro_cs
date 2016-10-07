# stats.py

from math import sqrt

def main():
    print('This program computes mean, median and standard deviations.')

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    med = median(data)

    print('\nThe mean is', xbar)
    print('The standard deviaton is', std)
    print('The median is', med)

def getNumbers():
    data = []
    xStr = input('Enter a number (<Enter> to quit) >> ')
    while xStr != '':
        data.append(eval(xStr))
        xStr = input('Enter a number (<Enter> to quit) >> ')
    return data

def mean(data):
    sums = 0.0
    for num in data:
        sums += num
    return sums / len(data)

def stdDev(data, xbar):
    sumDevSq = 0.0
    for num in data:
        dev = num - xbar
        sumDevSq += dev * dev

    return sqrt(sumDevSq / (len(data) - 1))

def median(data):
    data.sort()
    size = len(data)
    midPos = size // 2
    if size % 2 == 0:
        median = (data[midPos - 1] + data[midPos + 1]) / 2.0
    else:
        median = data[midPos]
    return median

if __name__ == '__main__': main()
