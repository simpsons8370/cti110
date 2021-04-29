#Random Math Quiz Program
#April 29, 2021
#CTI-110 P5HW2 - Math Quiz
#Shaunice Simpson
#

import random

print('Welcome to Math Quiz')
print()
            
def main_menu():
    while True:
        print()
        print('MAIN MENU')
        print('-'*20)
        print('1. Addition Random Numbers')
        print('2. Subtract Random Numbers')
        print('3. Exit')
        print()
        user_choice = int(input('Please choose one of the menu options: '))
        if user_choice == 1:
            adding_quiz()
        elif user_choice == 2:
            subtract_quiz()
        elif user_choice == 3:
            print('Thank you for playing...')
            print('Bye!!')
            break

def adding_quiz():
    total = 1
    num_1 = random.randint(0,50)
    num_2 = random.randint(0,50)
    correct_ans = num_1+num_2
    print(' ', num_1)
    print('+', num_2)
    print()
    print('Enter answer.')
    user_ans = int(input())
    while user_ans != correct_ans:
        if user_ans < correct_ans:
            print('Sorry, guess is too low.')
            print()
            user_ans = int(input('try again: '))
            total += 1
        elif user_ans > correct_ans:
            print('Sorry, guess is too high.')
            print()
            user_ans = int(input('try again: '))
            total += 1
    print('Congratulations!!!! your answer is correct..')
    print('Number of guesses: ', total)

def subtract_quiz():
    total = 1
    num_1 = random.randint(1,50)
    num_2 = random.randint(1,50)
    correct_ans = num_1-num_2
    print(' ', num_1)
    print('-', num_2)
    print()
    user_ans = int(input('Enter answer. '))
    while user_ans != correct_ans:
        if user_ans < correct_ans:
            print('Sorry, guess is too low.')
            print()
            user_ans = int(input('try again: '))
            total += 1
        elif user_ans > correct_ans:
            print('Sorry, guess is too high.')
            print()
            user_ans = int(input('try again: '))
            total += 1
    print('Congratulations!!!! your answer is correct..')
    print('Number of guesses: ', total)

main_menu()


#Program displays the main menu.
#Program ask user to pick a menu choice.
#If user choose option 1 or 2, the program executes the
#adding fuction or the subtraction function.
#Within both fuctions, the program sets a total counter variable
#and assigns 2 variables with random numbers.
#Program assigns the sum or difference between the 2 random numbers to a varable.
#Program displays the addition problem or subtraction problem to the user.
#Program ask user to enter the answer of the sum or difference of the math problem.
#If the user answer is less than the correct sum or difference, a message displays
#the guess is too low and to try again.
#If the user answer is greater than the correct sum or difference, a message displays
#the guess is too high and to try again.
#Every input increases the total counter variable by 1.
#If user answer is equal to the correct sum or difference, a message displays a
#congratulations and displays the total counter of guesses the user made.
#The program displays the main menu again for user to make another choice.
#If user choose option 3, the program displays a thank you for playing message,
#bye and terminates.

            
                    
                



        
        

