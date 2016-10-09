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



def mean(nums):
    sums = 0.0
    for num in data:
        sums += num
    return sums / len(data)

def stdDev(nums:
    sumDevSq = 0.0
    xbar = mean(nums)
    for num in data:
        dev = num - xbar
        sumDevSq += dev * dev

    return sqrt(sumDevSq / (len(data) - 1))

def median(nums):
    data.sort()
    size = len(data)
    midPos = size // 2
    if size % 2 == 0:
        median = (data[midPos] + data[midPos - 1]) / 2.0
    else:
        median = data[midPos]
    return median

if __name__ == '__main__': main()
