import re

def is_allowed_specific_char(s):
    """
    Check if a string contains only a-z, a-z, and 0-9 characters.
    """
    pattern = "^[a-zA-Z0-9]+$"
    return bool(re.match(pattern, s))