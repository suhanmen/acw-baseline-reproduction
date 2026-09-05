import re

def check_String(s: str) -> bool:
    """
    Check whether a string has at least one letter and one number.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string contains at least one letter and one number, False otherwise.
    """
    if not isinstance(s, str):
        return False

    has_letter = any(c.isalpha() for c in s)
    has_number = any(c.isdigit() for c in s)

    return has_letter and has_number