import re
import sys
import os

def load_common_passwords(password_strength_analyzer):
    try:
        with open(password_strength_analyzer, 'r') as file:
            return [line.strip() for line in file.readlines()] 
    except FileNotFoundError:
        print(f"Error: The file {password_strength_analyzer} was not found.")
        return []

common_passwords = load_common_passwords('common_passwords.txt')

def is_common_password(password, common_passwords):
    return password in common_passwords

def check_strength(password, common_passwords):
    if is_common_password(password, common_passwords):
        return "Very Weak (This is a commonly used password)"

    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[\W_]', password))

    if length < 8:
        return "Very Weak"
    elif not has_upper or not has_lower or not has_digit or not has_special:
        return "Weak"
    elif length >= 8 and length < 12:
        return "Moderate"
    elif length >= 12 and length < 16:
        return "Strong"
    else:
        return "Very Strong"

def main():
    password_strength_analyzer = 'common_passwords.txt'
    common_passwords = load_common_passwords(password_strength_analyzer)
    print("Starting the script...")
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password you would like to analyze: ")

    print(f"Password entered: {password}")

    strength = check_strength(password, common_passwords)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
    
