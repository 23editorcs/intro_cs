# Average Words Length
# wordLength.py

# Get a sentence, remove the trailing spaces.
# Count the length of a sentence.
# Count the number of words.
# Calculate the spaces = the number of words - 1
# The average = (the length - the spaces) / the number of words

def main():
    # Introduction
    print('The program calculates the average length of words in a sentence.')
    # Get a sentence
    sentence = input('Enter a sentence: ').rstrip()
    # Seperate it into words
    words = sentence.split()
    # Calculate the average length of words
    average = (len(sentence) - (len(words) - 1)) / len(words)
    # Rule them all
    print('Your average length of words is {0:.2f}.'.format(average))

main()
