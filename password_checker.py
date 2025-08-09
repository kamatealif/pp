"""
 Challenge: Password Strength Checker & Suggestion Tool

Build a Python script that checks the strength of a password based on:
1. Length (at least 8 characters)
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one digit
5. At least one special character (e.g., @, #, $, etc.)

Your program should:
- Ask the user to input a password.
- Tell them what's missing if it's weak.
- If the password is strong, confirm it.
- Suggest a strong random password if the input is weak.

Bonus:
- Hide password input using `getpass` (no echo on screen).
"""

import random 
import getpass
import string

def check_password(password):
    issues = []
    if len(password) < 8:
        issues.append("password should be 8 digits long!")
    if not any(char.islower() for char in password):
        issues.append("password must have a one lowerCase Letter!")
    if not any(char.isupper() for char in password):
        issues.append("password must have a one upperCase Letter!")
    if not any(char.isdigit() for char in password):
        issues.append("password must have a one digit!")
    if not any(char in string.punctuation for char in password):
        issues.append("password must have a one special character!")
    return issues


def generate_password(length=12):
    pass_str = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.sample(pass_str, length))

if __name__ == "__main__":
    password = getpass.getpass("Enter your password: ")
    issues = check_password(password)


    if not issues:
        print("Password is strong!")
    else:
        print("weak Password found:")
        for issue in issues:
            print("- " + issue)
    is_suggest = input("Would you like to suggest a strong password[y/n]: ")
    if is_suggest == 'y':
        length = int(input("Enter password length: "))
        print("Your Strong Password is: " + generate_password(length))


