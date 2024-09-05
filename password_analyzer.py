import re
import sys

#I used the Top 20 most common passwords according to Nordpass on Wikipedia
common_passwords = ['123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123', '1234567890', '1234567', 'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123']

def is_common_password(password):
    return password in common_passwords

def check_strength(password):
    if is_common_password(password):
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
    print("Starting the script...")
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password you would like to analyze: ")

    print(f"Password entered: {password}")

    strength = check_strength(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()
    
