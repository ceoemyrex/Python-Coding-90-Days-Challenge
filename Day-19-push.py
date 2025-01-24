# Project:
# Create a simple encryption/decryption tool using the cryptography library (e.g., AES encryption).


from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Function to generate a random key and IV
def generate_key_iv():
    key = os.urandom(32)  # AES-256 requires a 32-byte key
    iv = os.urandom(16)   # IV should be 16 bytes for AES
    return key, iv

# Function to encrypt plaintext
def encrypt(plaintext, key, iv):
    # Pad the plaintext to make it a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()

    # Initialize the AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return ciphertext

# Function to decrypt ciphertext
def decrypt(ciphertext, key, iv):
    # Initialize the AES cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Unpad the plaintext
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext.decode()

# Example usage
if __name__ == "__main__":
    # Generate key and IV
    key, iv = generate_key_iv()

    # Original plaintext message
    plaintext = "This is a secret message."

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key, iv)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt(ciphertext, key, iv)
    print(f"Decrypted Text: {decrypted_text}")
