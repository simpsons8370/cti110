# Define your function here 
def steps_to_miles(user_steps):
    return user_steps/2000

if __name__ == '__main__':
    # Type your code here.
    steps = float(input())
    print('{:.2f}'.format(steps_to_miles(steps)))