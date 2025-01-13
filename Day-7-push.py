

def main():
    user_data = {}  # Dictionary to store user information

    while True:
        print("\nMenu:")
        print("1. Add User Information")
        print("2. Retrieve User Information")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Add user information
            name = input("Enter the user's name: ").strip()
            if name in user_data:
                print(f"User '{name}' already exists.")
            else:
                try:
                    age = int(input("Enter the user's age: ").strip())
                    user_data[name] = age
                    print(f"User '{name}' added successfully!")
                except ValueError:
                    print("Invalid age! Please enter a valid number.")

        elif choice == '2':
            # Retrieve user information
            name = input("Enter the name to retrieve information: ").strip()
            if name in user_data:
                print(f"Name: {name}, Age: {user_data[name]}")
            else:
                print(f"No user found with the name '{name}'.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option (1/2/3).")


if __name__ == "__main__":
    main()
