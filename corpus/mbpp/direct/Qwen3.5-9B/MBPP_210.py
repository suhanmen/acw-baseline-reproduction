import re

def is_allowed_specific_char(s: str) -> bool:
    """
    Check if the string contains only lowercase letters (a-z), uppercase letters (A-Z),
    and digits (0-9).
    """
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.fullmatch(pattern, s))

# Example assertions (uncomment to test):
# assert is_allowed_specific_char("ABCDEFabcdef123450") == True
# assert is_allowed_specific_char("*&%@#!}{") == False
# assert is_allowed_specific_char("HELLOhowareyou98765") == True