''' Type your code here. '''
number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

if (number_1 <= number_2) and (number_1 <= number_3):
       smallest_number = number_1
elif (number_2 <= number_1) and (number_2 <= number_3):
       smallest_number = number_2
else:
       smallest_number = number_3
       
print(smallest_number)