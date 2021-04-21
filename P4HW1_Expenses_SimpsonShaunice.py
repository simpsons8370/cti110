#CTI - 110
#P4HW1 - Expenses
#Shaunice Simpson
#April 20, 2021

count = 1
expense = 0
total_sum = 0
again = 'y'

starting_amount = float(input('Enter starting amount in account $'))
print()

while again == 'y':
    expense = float(input('Enter expense '+str(count)+': '))
    total_sum = total_sum + expense
    again = input('Do you want to enter another expense? (y/n) ')
    print()
    if again == 'y':
        count = count + 1

total_amount = starting_amount - total_sum
print('Amount in account before expenses substracted $'+str(starting_amount))
print('Number of expenses entered: '+str(count))
print('Amount in account after expenses subtracted is $'+str(total_amount))
                    
#Program asks user for the starting amount
#While the again variable is set to 'y', the program asks user input of expenses
#The total_sum is calculated as total_sum (starts at 0) plus the expenses entered
#Program asks user if another expenses will be entered
#If yes, the count variable is increased by 1, and another expense is entered
#The added expense is calculated into the total_sum variable
#Once the user stops entering in expenses, the program displays results
#The total_amount is calculated as the starting amount minus the total_sum
#Program displays the starting amount in a string
#Program displays the number of expenses entered, which is the count in a string
#Program displays the total_amount in a string


