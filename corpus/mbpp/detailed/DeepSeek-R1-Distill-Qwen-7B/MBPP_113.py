import re

def check_integer(s):
    """
    Check if a string represents an integer.
    """
    # Check if the string is empty
    if not s:
        return False

    # Regex pattern for valid integers
    pattern = r'^[+-]?\d+$'

    # Check if the string matches the pattern
    return bool(re.match(pattern, s))

# Test cases
assert check_integer("python") == False
assert check_integer("1") == True
assert check_integer("12345") == True