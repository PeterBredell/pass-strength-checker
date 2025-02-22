import re
import random
import string

def check_password_strength(password):
    
    if len(password) < 12: # Works somewhat as a base case
        return "Password may be too short"
    
    if not re.search(r"[A-Z]", password): # Learned that the r prefix tells Python it’s a raw string (so backslashes aren’t treated as escape characters)
        return "Weak: Missing uppercase letters"
    if not re.search(r"[a-z]",password):
        return "Weak: Missing lowercase letters"
    if not re.search(r"\d", password):
        return "Weak: Missing numbers"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Missing special characters"
    
    common_passwords = ["123456", "password", "12345678", "qwerty", "123456789", "12345", "1234", "111111", "1234567", "dragon", "123123", "baseball", "abc123", "football", "monkey", "letmein", "696969", "shadow", "master", "666666", "qwertyuiop", "123321", "mustang", "1234567890", "michael", "654321", "pussy", "superman", "1qaz2wsx", "7777777", "fuckyou", "121212", "000000", "qazwsx", "123qwe", "killer", "trustno1", "jordan", "jennifer", "zxcvbnm", "asdfgh", "hunter", "buster", "soccer", "harley", "batman", "andrew", "tigger", "sunshine", "iloveyou", "fuckme", "2000", "charlie", "robert", "thomas", "hockey", "ranger", "daniel", "starwars", "klaster", "112233", "george", "asshole", "computer", "michelle", "jessica", "pepper", "1111", "zxcvbn", "555555", "11111111", "131313", "freedom", "777777", "pass", "fuck", "maggie", "159753", "aaaaaa", "ginger", "princess", "joshua", "cheese", "amanda", "summer", "love", "ashley", "6969", "nicole", "chelsea", "biteme", "matthew", "access", "yankees", "987654321", "dallas", "austin", "thunder", "taylor", "matrix",]

    # Found a list of most common passwords on wikipedia - hindsight could have removed all of the passwords on the list that is shorter than 12 characters

    if password.lower() in common_passwords:
        return "Weak: Password is a commonly used password"
    
    return "Great Password!"

def generate_strong_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(16))

password = input("Enter a password to check: ")
print(check_password_strength(password))

if (check_password_strength(password) != "Great Password!"):
    print("Recommended stronger password : " + generate_strong_password())