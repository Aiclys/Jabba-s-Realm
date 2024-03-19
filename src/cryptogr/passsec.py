#!/usr/bin/env python3
import string
import secrets
import math
import hashlib

def genpass(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(all_characters) for i in range(length))
    return password

def genpassphrase(length):
    word_file = open("wordlist.txt", "r")
    word_list = []
    passphrase = ""

    for word in word_file:
        word_with_space = word
        word_list.append(word_with_space)

    passphrase_list = [secrets.choice(word_list) for i in range(length)]
    for word in passphrase_list:
        e = 0
        for letter in word:
            e += 1

        new_line = word[e-1:]
        word_without_new_line = word[:e-1]
        passphrase += " " + word_without_new_line

    passphrase = passphrase[1:]
    return passphrase

print(genpassphrase(4))

def password_entropy(password, numeric_form):
    alphabet_lower = [letter for letter in string.ascii_letters][:26]
    alphabet_upper = [letter for letter in string.ascii_letters][27:]
    digits = [digit for digit in string.digits]
    punctuation = [i for i in string.punctuation]
    entropy_in_decimal = 1

    for character in password:
        if character in alphabet_lower:
            entropy_in_decimal = entropy_in_decimal * 26
        elif character in alphabet_upper:
            entropy_in_decimal = entropy_in_decimal * 26
        elif character in digits:
            entropy_in_decimal = entropy_in_decimal * 10
        elif character in punctuation:
            entropy_in_decimal = entropy_in_decimal * 32

    entropy_in_bits = math.log(entropy_in_decimal, 2)
    entropy_in_bytes = entropy_in_bits / 8

    if numeric_form == "decimal":
        return entropy_in_decimal
    elif numeric_form == "bits":
        return entropy_in_bits
    elif numeric_form == "bytes":
        return entropy_in_bytes

def password_safety(password):
    if password_entropy(password, "bits") < 35 and password_entropy(password, "bits") < 50:
        return "very weak"
    elif password_entropy(password, "bits") >= 50 and password_entropy(password, "bits") < 75:
        return "weak"
    elif password_entropy(password, "bits") >= 75 and password_entropy(password, "bits") < 95:
        return "medium"
    elif password_entropy(password, "bits") >= 95 and password_entropy(password, "bits") < 125:
        return "strong"
    elif password_entropy(password, "bits") >= 125:
        return "very strong"

def hashpass(password):
    encoded_password = bytes(password, "utf-8")
    hashed_password = hashlib.sha512(encoded_password)
    password_hash = hashed_password.hexdigest()
    return password_hash

