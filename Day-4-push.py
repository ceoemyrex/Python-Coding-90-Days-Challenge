# Project
#  Create a simple "countdown" program that counts down from 10 to 1 using a while loop.

def countdown():
    number = 10  # Starting number
    while number > 0:  # Loop continues as long as the number is greater than 0
        print(number)
        number -= 1  # Decrement the number by 1
    print("Liftoff!")  # Message after the countdown ends

# Run the countdown function
countdown()
