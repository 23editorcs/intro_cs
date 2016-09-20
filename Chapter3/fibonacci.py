# Fibonacci
# fibonacci.py

def main():
    # Instruction
    print('The program calculates Fibonacci number.')
    # Get the n number
    n = eval(input('How many numbers do you want?(>2) '))
    # Calculate fibonacci
    f1 = 1
    f2 = 1
    for i in range(2, n):
        fibo = f1 + f2
        f1 = f2
        f2 = fibo
    # Rule them all
    print('Your Fibonacci number is', fibo)

main()
