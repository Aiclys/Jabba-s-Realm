#!/usr/bin/env python3

# Imports
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64
import getpass


# Generate the salt used for key derivation in the scrypt algorithm, default length=16 bytes
def gen_salt(length=16):
    return secrets.token_bytes(length)

# Function for deriving the key from the chosen password with the salt
def derive_key(passwd, salt):
    scr_kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return scr_kdf.derive(passwd.encode())

# Load and create salt from a file
def create_saltfile():
    saltfile = open("salt.salt", "rb")
    return saltfile.read()

# Generate the key
def generate_key(password, salt_length=16, use_existing_salt=False, save_salt=True):
    if load_existing_salt:
        # load existing salt
        salt = load_salt()
    elif save_salt:
        salt = generate_salt(salt_length)
        with open("salt.salt", "wb") as salt_file:
            salt_file.write(salt)
    derived_key = derive_key(salt, password)
    encoded_key = base64.urlsafe_b64encode(derived_key)
    return encoded_key

# Encrypt the file
def encrypt(filename, key):
    fer = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = fer.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

# Decrypt the file
def decrypt(filename, key):
    fer = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    try:
        decrypted_data = f.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print("Invalid token, most likely the password is incorrect")
        return
    with open(filename, "wb") as file:
        file.write(decrypted_data)
