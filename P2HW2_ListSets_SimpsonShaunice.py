#CTI-110
#P2HW2 - List and Sets
#Shaunice Simpson
#March 3, 2021
#

input_list = []

print('Enter a series of 10 numbers')
input_list.append(int(input('Number 1: ')))
input_list.append(int(input('Number 2: ')))
input_list.append(int(input('Number 3: ')))
input_list.append(int(input('Number 4: ')))
input_list.append(int(input('Number 5: ')))
input_list.append(int(input('Number 6: ')))
input_list.append(int(input('Number 7: ')))
input_list.append(int(input('Number 8: ')))
input_list.append(int(input('Number 9: ')))
input_list.append(int(input('Number 10: ')))
print()
print('Lowest number in the list: ', min(input_list))
print('Highest number in the list: ', max(input_list))
print('Total of the numbers in the list: ', sum(input_list))
print('Average of the numbers in the list: ', sum(input_list) / len(input_list))
print()
input_set = set(input_list)
print(input_set)

#Program prompts user to enter a series of 10 numbers
#Program asks for input for numbers 10 times
#Program creates a list from the user input
#Program displays the lowest number in the list
#Program displays the highest number in the list
#Program displays the sum of the numbers in the list
#Program dispalys the average of the numbers in the list
#Program creates the list into a set
#Program displays the set
