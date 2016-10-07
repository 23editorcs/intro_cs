# prime.py
# The Sieve of Eratosthenes


def main():
    print('This program returns a list of prime number that less than n')
    n = int(input('Enter a number: '))
    listOfPrime = sieve(n)
    print(listOfPrime)

def sieve(n):
    # Find the prime number to n by Sieve of Eratosthenes
    nums = list(range(2,n + 1))
    for num in nums:
        i = 2
        while num * i <= n:
            if num * i in nums:
                nums.remove(num * i)
            i += 1
    return nums
    
if __name__ == '__main__': main()
