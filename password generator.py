import random
import string

def generate_password(min_length, numbers=True, special_char=True):
    letter = string.ascii_letters
    digit = string.digits
    special = string.punctuation

    characters = letter
    if numbers:
        characters += digit
    if special_char:
        characters += special


    pwd = ""
    meet_criteria = False
    has_num = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digit:
            has_num = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_num
        if special_char:
            meet_criteria = meet_criteria and has_special

    return pwd 


min_length = int(input("Enter the minimum length: "))
has_num = input("Do you want to have a numbers (y/n)? ").lower() == "y"
has_special = input("Do you wna to have special characers (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_num, has_special)
print("The generated password is:", pwd)