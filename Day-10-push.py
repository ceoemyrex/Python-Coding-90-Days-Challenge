# Project:
# Write a Python script that calculates the square root of a number using the math library.

import math

def calculate_square_root(number):
    """Calculates the square root of a number.

    Args:
        number: The number for which to calculate the square root.

    Returns:
        The square root of the number, or None if the input is invalid.
        Prints an error message to the console if there is an error.
    """
    try:
        if not isinstance(number, (int, float)):
            raise TypeError("Input must be a number (integer or float).")
        if number < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")

        result = math.sqrt(number)
        return result
    except TypeError as e:
        print(f"Type Error: {e}")
        return None
    except ValueError as e:
        print(f"Value Error: {e}")
        return None
    except Exception as e: # Catches any other unexpected error
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        num = float(user_input)  # Attempt to convert to float to handle integers and decimals

        sqrt_result = calculate_square_root(num)

        if sqrt_result is not None:
            print(f"The square root of {num} is: {sqrt_result}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except EOFError:
        print("\nInput ended.")
    except Exception as e:
        print(f"An unexpected error occurred during input: {e}")