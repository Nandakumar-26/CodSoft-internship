
# Task 3: Password Generator

import random
import string

def generate_password():
    print("\n--- PASSWORD GENERATOR ---")

    length = int(input("Enter desired password length: "))

    if length < 4:
        print("Password length should be at least 4 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("Generated Password:", password)

generate_password()