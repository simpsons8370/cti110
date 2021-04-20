#CTI - 110
#P4HW2 - Distance Traveled
#Shaunice Simpson
#April 15, 2021
#


def main():
    again = 'y'
    while again == 'y':
        car_speed = float(input('Enter car\'s speed: '))
        time_traveled = int(input('Enter time traveled: '))
        if time_traveled <= 0:
            print()
            print('Error! time entered should be >0')
            time_traveled = int(input('Enter time traveled: '))
        print()
        print('Time    Distance')
        print('-'*17)
        for i in range(1,time_traveled+1):
            print('{}       {}'.format(i,car_speed*i))
        again = input('would you like to enter a different time? (y for yes): ')

main()

#A varable is created for user to input a different time
#While the variable loop is equal to 'y', the user inputs a speed and time traveled
#The program will loop as long as the time traveled is not less than or equal to 0
#User is shown an error message and asks for another input for time traveled
#The program will loop from 1 to time traveled input
#Program will calculate, car speed x time traveled
#Program will display data in a table
#User will be asked if a different time will be entered
