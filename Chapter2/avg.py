# Average of Scores
# avg.py

def main():
    # Instruction
    print('The program calculates the average scores.')
    # Get scores from the user
    score1, score2, score3 = eval(input('Enter scores (separate by comma): '))
    # Calculate the average
    avg = (score1 + score2 + score3) / 3
    # Rule them all
    print('Your Average score is:', avg)

main()
