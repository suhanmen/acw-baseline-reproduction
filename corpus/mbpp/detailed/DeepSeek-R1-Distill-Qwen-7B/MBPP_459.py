import re

def remove_uppercase(s):
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    # Use regex to remove all uppercase letters
    return re.sub(r'[A-Z]', '', s)