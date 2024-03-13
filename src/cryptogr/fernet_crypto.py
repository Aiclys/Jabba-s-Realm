#!/usr/bin/env python3
from cryptography.fernet import Fernet

def generate_key():

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def read_key():
    return open("key.key", "rb").read()

def crypt_text(text, mode):
    # write and generate the key
    generate_key()

    # load and read the key
    key = read_key()

    # encode the message because it needs to ber converted to bytes before being encrypted
    encoded_text = text.encode()

    fer = Fernet(key)
    if mode == "encrypt":
        encrypted_text = fer.encrypt(encoded_text)
        return encrypted_text
    elif mode == "decrypt":
        decrypted_text = fer.decrypt(text)
        return decrypted_text
