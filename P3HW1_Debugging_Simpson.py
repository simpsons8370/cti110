#CTI - 110
#P3HW1 - Debugging
#Shaunice Simpson
#March 23, 2021
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    # TO DO: define the rest of the scores
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score and score < A_score:
            print('Your grade is: B')
        else:
            if score >= C_score and score < B_score:
                print('Your grade is: C')
            else:
                if score >= D_score and score < C_score:
                    print('Your grade is: D')
                else:
                    print('Your grade is: F') # TO DO: finish this







# program start
main()
