#A Guessing Game Program
#April 27, 2021
#CTI-110 P5HW1 - Random Number
#Shaunice Simpson
#



import random

def guessing_game(number):
    g = 0
    while new == '1':
        guess_num = int(input('Guess a number: '))
        if guess_num > number:
            print('Too high, try again')
            g = g + 1
        elif guess_num < number:
            print('Too low, try again')
            g = g + 1
        elif guess_num == number:
            print('Congratulations! You have guessed the number correctly in', g+1,'tries.')
            break
        
if __name__ == '__main__':
    print('MAIN MENU')
    print()
    print('-'*13)
    print()
    print()
    print('1) Play Game')
    print('2) Exit')
    new = '1'
    while new == '1':
        number = random.randint(1,100)
        guessing_game(number)

        new = input('Would you like to play again? (1 - yes, 2 - no)')

#The program imports the random module.
#The program generates a random number.
#The program asks the user to guess a number.
#If the guessed number is greater than the generated number a message appears that the number is
#too high and try again.
#If the guessed number is less than the generated number a message appears that the number is
#too low and try again.
#If the guessed number is equal to the generated number a message appears that the number is
#correctly guessed and how many tries it took.
#The program asks the user if they would like to try again.
