# - Project:
# Write a function that takes a number as input and returns the factorial of that number.

def factorial(n):
    """
    Calculate the factorial of a number.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of the input number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
    
#example
    number = 7
print(f"The factorial of {7} is {factorial(10)}.")