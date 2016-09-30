# Fibonacci
# fibo.py

def main():
    n = eval(input('Enter a number: '))
    i = 2
    f1 = 1
    f2 = 1
    fn = 1
    while i < n:
        fn = f1 + f2
        f1 = f2
        f2 = fn
        i += 1
    print(fn)

main()
