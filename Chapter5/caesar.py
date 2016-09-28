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
    # Get a origin file name & the encrypt file name
    infileName = input('Enter the origin file name: ')
    outfileName = input('Where do we put the secret message: ')
    # Open 2 files
    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')
    # Read the infile line by line
    for line in infile:
        # Get a message and a key, seperate by a dot.
        lines = line.split('.')
        message = lines[0]
        key = eval(lines[1])
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
        print('{0}'.format(encrypt), file = outfile)
    infile.close()
    outfile.close()

main()
