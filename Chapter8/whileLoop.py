# Chapter 8 Discussion

# Sum of n counting numbers
''' i = 1
while i <= n:
    sums = sums + i
    i += 1

# Sum of the first n odd numbers
i = 1
while i < 2 * n:
    sums = sums + i
    i += 2

# Sum of a series of number entered by the user until the value 999 is entered.
def main():
    x = 1
    sums = 0
    while x != 999:
        sums = sums + x
        x = eval(input('Enter a number (999 to quit): '))
        print(x)
    print(sums)
    print(x)
'''
def main():
    n = 100
    count = 0
    while n >= 2:
        count += 1
        n = n // 2
    print(count)

main()
