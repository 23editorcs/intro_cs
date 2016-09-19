# Coffee Shop
# coffee.py

def main():
    # Instruction
    print('The program calculates the price from coffee order.')
    # Get the pound input
    order = eval(input('How much do you buy? '))
    # Calculate the order's price
    price = order * (10.50 + 0.86) + 1.50
    # Rule them all
    print('Your order is ${0:.2f}.'.format(price))
main()
