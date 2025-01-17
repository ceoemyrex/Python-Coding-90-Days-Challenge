#- Project:
#Build a program that validates email addresses using regular expressions.


import re

def is_valid_email(email):
    """
    Checks if a given string is a valid email address using a regular expression.

    Args:
        email: The string to check.

    Returns:
        True if the string is a valid email address, False otherwise.
    """

    # Regular expression for email validation (more robust)
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.fullmatch(email_regex, email):
        return True
    else:
        return False

if __name__ == "__main__":
    emails_to_test = [
        "onuohaemma167@gmail.com",
        "ceonetworktech@gmail.com",

    ]

    for email in emails_to_test:
        if is_valid_email(email):
            print(f"'{email}' is a valid email address.")
        else:
            print(f"'{email}' is NOT a valid email address.")

    while True:
        user_email = input("Enter an email address to validate (or type 'exit'): ")
        if user_email.lower() == "exit":
            break
        if is_valid_email(user_email):
            print(f"'{user_email}' is a valid email address.")
        else:
            print(f"'{user_email}' is NOT a valid email address.")