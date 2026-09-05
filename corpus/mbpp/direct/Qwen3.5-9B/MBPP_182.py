import re

def find_character(s: str):
    # Match all uppercase letters
    upper = re.findall(r'[A-Z]', s)
    # Match all lowercase letters
    lower = re.findall(r'[a-z]', s)
    # Match all special characters (not alphanumeric)
    special = re.findall(r'[^a-zA-Z0-9]', s)
    # Match all numeric digits
    numeric = re.findall(r'[0-9]', s)
    return (upper, lower, special, numeric)