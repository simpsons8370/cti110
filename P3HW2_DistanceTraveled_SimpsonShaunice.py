#CTI - 110
#P3HW2 - Distance Traveled
#Shaunice Simpson
#March 23, 2021
#


car_speed = float(input('Enter car\'s speed: '))
time_traveled = float(input('Enter time traveled: '))

def main():
    print('Speed entered: ', car_speed)
    print('Time entered: ', time_traveled)
    print()
    distance_traveled = car_speed * time_traveled
    print('Distance Traveled', distance_traveled, 'miles')

if time_traveled <= 0:
    print()
    print('Error ! time entered should be >0')
    time_traveled = 1
    distance_traveled = car_speed * time_traveled
    print()
    print('Speed entered:', car_speed)
    print('Time:', time_traveled)
    print()
    print('Distance Traveled', distance_traveled, 'miles')
else:
    main()


#User inputs the car speed
#User inputs the time traveled
#If time traveled input is less than 0, program executes and displays error message
#Program displays the speed entered by user
#Program displays the time traveled as 1
#Program multiples the speed and time and displays the product in miles
#Else, programs calls the main function
#Program displays the speed entered by user
#Program displays the time traveled
#Program multiplies the speed and time and displays the product in miles
