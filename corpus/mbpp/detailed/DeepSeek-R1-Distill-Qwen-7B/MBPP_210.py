import re

def is_allowed_specific_char(s):
    """
    Check if the given string contains only a-z, A-Z, and 0-9 characters.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string contains only allowed characters, False otherwise.
    """
    # Define the allowed characters using a regular expression
    allowed_chars_pattern = '[a-zA-Z0-9]'

    # Check if the string matches the pattern
    return bool(re.fullmatch(allowed_chars_pattern, s))