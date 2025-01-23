#- Project:
#Write a Python script that hashes a user’s password and compares it to a known hash.


import hashlib
import os

def hash_password(password, salt=None):
    """Hashes a password using SHA-256 with optional salting."""

    if salt is None:
        # Generate a random salt if one isn't provided. This is CRUCIAL for security.
        salt = os.urandom(16)  # 16 bytes is a good length for a salt

    salted_password = salt + password.encode('utf-8')  # Encode password to bytes
    hashed_password = hashlib.sha256(salted_password).hexdigest()

    return hashed_password, salt.hex()  # Return the hash and the salt (hex encoded)

def verify_password(password, stored_hash, stored_salt):
    """Verifies a password against a stored hash and salt."""
    try:
        salt = bytes.fromhex(stored_salt) #Convert hex string salt back to bytes
        hashed_password, _ = hash_password(password, salt)
        return hashed_password == stored_hash
    except ValueError:
        return False #Return false if the salt is invalid hex

# Example usage (Storing a new password):
def store_new_password():
    password = input("Enter a new password: ")
    hashed_password, salt = hash_password(password)

    # In a real application, you would store the hashed_password AND the salt in your database.
    print(f"Hashed password: {hashed_password}")
    print(f"Salt: {salt}")

    #Example of storing in a file. NOT RECOMMENDED for production. Use a database.
    with open("credentials.txt", "w") as f:
        f.write(f"{hashed_password}\n{salt}")

#Example usage (verifying password)
def verify_stored_password():
    try:
        with open("credentials.txt", "r") as f:
            stored_hash, stored_salt = f.read().splitlines()
    except FileNotFoundError:
        print("No credentials stored. Please store a password first.")
        return

    password = input("Enter password to verify: ")
    if verify_password(password, stored_hash, stored_salt):
        print("Password verified!")
    else:
        print("Incorrect password.")

if __name__ ==