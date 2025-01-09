#  Project:
# Build a simple age checker: Ask the user for their age and tell them if they are eligible for certain services (e.g., "You are eligible to vote" or "You are too young to vote").


def main():
    # Ask the user for their age
    age = int(input("Please enter your age: "))

    # Check eligibility for services
    if age >= 18:
        print("You are eligible to vote.")
        if age >= 21:
            print("You are also eligible to purchase alcohol (depending on your country's laws).")
    else:
        print("You are too young to vote.")

if __name__ == "__main__":
    main()