import re
from typing import Tuple, Union

def _is_valid_binary_string(input_string: Union[str, None]) -> Tuple[bool, str]:
    """
    Validates the input string and checks if it consists solely of binary digits (0 and 1).

    Args:
        input_string: The string to validate.

    Returns:
        A tuple containing:
        - A boolean indicating if the string is a valid binary string.
        - An error message if validation fails, otherwise an empty string.
    """
    if input_string is None:
        return False, "Input is None"

    if not isinstance(input_string, str):
        return False, f"Input type is not str, got {type(input_string).__name__}"

    if len(input_string) == 0:
        return False, "Input string is empty"

    binary_pattern = re.compile(r'^[01]+$')

    if not binary_pattern.match(input_string):
        return False, "String contains non-binary characters"

    return True, ""

def check(input_string: Union[str, None]) -> str:
    """
    Checks whether the given string is a binary string or not.

    A binary string is defined as a non-empty string containing only the characters '0' and '1'.

    Args:
        input_string: The string to check. Can be None, an empty string, or a string with any characters.

    Returns:
        "Yes" if the string is a valid binary string.
        "No" if the string is invalid, empty, or contains characters other than '0' and '1'.
    """
    if input_string is None:
        return "No"

    if not isinstance(input_string, str):
        return "No"

    if len(input_string) == 0:
        return "No"

    is_valid, error_message = _is_valid_binary_string(input_string)

    if is_valid:
        return "Yes"
    else:
        return "No"