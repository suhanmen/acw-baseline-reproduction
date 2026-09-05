import re
from typing import Union

# Pre-compiled regex pattern for matching decimal numbers with exactly 2 decimal places
# The pattern breakdown:
# ^asserts the start of the string
# -?\d* matches an optional minus sign followed by zero or more digits (integer part)
# \. matches the literal decimal point
# \d{2} matches exactly two digits (decimal part)
# $asserts the end of the string
DECIMAL_PATTERN = re.compile(r'^-?\d*\.\d{2}$')

def _is_valid_decimal_string(input_str: str) -> bool:
    """
    Validates if the input string represents a decimal number with exactly 2 decimal places.

    Args:
        input_str (str): The string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Check for None input type explicitly
    if not isinstance(input_str, str):
        return False

    # Check for empty string
    if len(input_str) == 0:
        return False

    # Use the pre-compiled regex to check against the pattern
    return bool(DECIMAL_PATTERN.match(input_str))

def is_decimal(value: Union[str, float, int, None]) -> bool:
    """
    Checks if the given value is a string representing a decimal number 
    with a precision of exactly 2 decimal places.

    This function strictly validates the string format and does not accept 
    floats, ints, or None, as the problem context implies string validation 
    based on the provided test cases ('123.11', '0.21', etc.).

    Args:
        value: The value to check. Expected to be a string.

    Returns:
        bool: True if the value is a valid decimal string with 2 decimal places, False otherwise.
    """
    # Validate input type: must be a string
    if not isinstance(value, str):
        return False

    # Delegate to the detailed validation helper
    return _is_valid_decimal_string(value)