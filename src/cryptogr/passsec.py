#!/usr/bin/env python3
import string
import secrets
import random
import math
import hashlib

def genpass(length, options):
    #all chars that can be in pass
    characters = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ["!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~"]]

    #defining all chars that'll be in this pass
    symbols = []
    for i in range(4):
        if options[i] == 'y':
            for j in characters[i]:
                symbols.append(j)

    #generating and returning pass
    chars = []
    for i in range(length):
        chars.append(symbols[random.randint(0, len(symbols)-1)])
    password = ''.join(chars)

    return password


def gen_passphrase(length):
    word_file = open("wordlist.txt", "r")
    word_list = []
    passphrase = ""

    for word in word_file:
        word_list.append(word)

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

def password_entropy(password, numeric_form="bits"):
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
        return int(entropy_in_bits)
    elif numeric_form == "bytes":
        return entropy_in_bytes

def password_safety(password):
    if password_entropy(password, "bits") < 35:
        return "very weak"
    elif password_entropy(password, "bits") >= 35 and password_entropy(password, "bits") < 60:
        return "weak"
    elif password_entropy(password, "bits") >= 60 and password_entropy(password, "bits") < 80:
        return "medium"
    elif password_entropy(password, "bits") >= 80 and password_entropy(password, "bits") < 115:
        return "strong"
    elif password_entropy(password, "bits") >= 115:
        return "very strong"

def gen_pass_with_entropy(min_entropy):
    check = None
    password = genpass()
    while check == None:
        if password_entropy(password, "bits") >= min_entropy:
           check = False
        else:
            password = genpass()

    return password

def gen_passphrase_with_entropy(min_entropy):
    check = None
    passphrase = gen_passphrase()
    while check == None:
        if password_entropy(passphrase, "bits") >= min_entropy:
           check = False
        else:
            passphrase = gen_passphrase()

    return passphrase

def hashpass(password, hash_func="sha512"):
    encoded_password = bytes(password, "utf-8")

    if hash_func == "sha512":
        hashed_password = hashlib.sha512(encoded_password)
    elif hash_func == "sha384":
        hashed_password = hashlib.sha384(encoded_password)
    elif hash_func == "sha256":
        hashed_password = hashlib.sha256(encoded_password)
    elif hash_func == "sha224":
        hashed_password = hashlib.sha224(encoded_password)
    elif hash_func == "sha3_512":
        hashed_password = hashlib.sha3_512(encoded_password)
    elif hash_func == "sha3_384":
        hashed_password = hashlib.sha3_384(encoded_password)
    elif hash_func == "sha3_256":
        hashed_password = hashlib.sha3_256(encoded_password)
    elif hash_func == "sha3_224":
        hashed_password = hashlib.sha3_224(encoded_password)
    elif hash_func == "shake256":
        hashed_password = hashlib.shake256(encoded_password)
    elif hash_func == "shake128":
        hashed_password = hashlib.shake128(encoded_password)

    password_hash = hashed_password.hexdigest()
    return password_hash

