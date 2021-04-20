first_num = int(input())
second_num = int(input())

if second_num < first_num:
    print('Second integer can\'t be less than the first.')
while first_num <= second_num:
        print(first_num, end=' ')
        first_num += 5
print()    