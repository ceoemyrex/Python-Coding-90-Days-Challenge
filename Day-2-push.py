# Project:
 #- Create a program that takes user input for their name and age, then prints a greeting with their name and calculates the year they were born.

from datetime import datetime

def main():
    # Get the current year
    current_year = datetime.now().year

    # Take user input for name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate the year of birth
    year_of_birth = current_year - age

    # Print the greeting and year of birth
    print(f"Hello, {name}! You were born in the year {year_of_birth}.")

if __name__ == "__main__":
    main()