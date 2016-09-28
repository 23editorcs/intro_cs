# Words Counting
# wordCount.py

def main():
    # Introduction
    print('The program counts the number of words in a sentence that you input.')
    # Get a sentence from user
    message = input('Type your sentence: ')
    # Seperate the sentence into words
    words = message.split()
    # Rule them all
    print('Your sentence has {0} words.'.format(len(words)))

main()
