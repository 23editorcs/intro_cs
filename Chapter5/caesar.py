# Caesar Cipher
# caesar.py

# A-Z: 65-90
# a-z: 97-122, the difference is 32
# For upper case: (num + key) % 91 + (num + key) // 91 * 65
# For lower case: (num + key) % 123 + (num + key) // 123 * 97
# For both: (num + key) % (91 + num // 97 * 32) +
    # (num + key) // (91 + num // 97 * 32) * (65 + num // 97 * 32)

def main():
    # Introduction
    print('The program encrypts a message by Caesar cipher.')
    # Get a message and a key
    message = input('Enter your message to encrypt: ')
    key = eval(input('What is the secret key.'))
    # Seperate the message into words
    words = message.split()
    # Create an encrypt message
    encrypt = ''
    # Encode the message word by word
    for word in words:
        for i in word:
            num = ord(i)
            numEncode = (num + key) % (91 + num // 97 * 32) + \
                        (num + key) // (91 + num // 97 * 32) * \
                        (65 + num // 97 * 32)
            encrypt = encrypt + chr(numEncode)
        encrypt = encrypt + " "
    # Rule them all
    print('Your message is {0}.'.format(encrypt))

main()
