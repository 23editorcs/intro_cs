# Five Quizzes
# fiveQuiz.py

def main():
    # Introduction
    print('The program prints the grade of a scores.')
 
    # Put thing in a try/except
    try:
        # Get the score
        score = eval(input('Enter the score: '))
        if score == 5:
            print('A')
        elif score == 4:
            print('B')
        elif score == 3:
            print('C')
        elif score == 2:
            print('D')
        elif score == 1:
            print('E')
        else:
            print('Not a good score.')
    except:
        print('Something is wrong')

if __name__ == '__main__':
    main()
