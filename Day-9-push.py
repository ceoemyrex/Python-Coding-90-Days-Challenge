#- Project:
#- Create a program that takes user input for a number and catches errors if the user inputs something invalid (non-integer).


def get_valid_integer_input(prompt):
    """
    Prompts the user for an integer and handles invalid input.

    Args:
        prompt: The message to display to the user.

    Returns:
        The integer entered by the user, or None if the input is invalid after multiple attempts.
    """
    max_attempts = 3  # Set a maximum number of attempts
    attempts = 0

    while attempts < max_attempts:
        try:
            user_input = input(prompt)
            num = int(user_input)
            return num  # Return the integer if conversion is successful
        except ValueError:
            attempts += 1
            print(f"Invalid input. Please enter a valid integer. Attempts remaining: {max_attempts - attempts}")

    print(f"Too many invalid attempts. Exiting after {max_attempts} attempts.")
    return None  # Return None if all attempts fail


if __name__ == "__main__":
    num = get_valid_integer_input("Enter a number: ")

    if num is not None:
        print(f"You entered: {num}")
        # You can now use the 'num' variable safely, as it's guaranteed to be an integer
        squared_num = num * num
        print(f"The square of your number is: {squared_num}")
    else:
        print("Could not get valid input.")