import re
from typing import Final

def is_decimal(value: str) -> bool:
    """
    Checks if a given string represents a decimal number with a precision
    of exactly 2 decimal places using regular expressions.

    A valid decimal in this context is defined as:
    1. A string representing a number.
    2. Containing exactly two digits after the decimal point.
    3. Supporting optional leading signs (+ or -).
    4. Supporting optional leading zeros.

    Args:
        value (str): The input string to validate.

    Returns:
        bool: True if the string is a decimal with precision of 2, False otherwise.
    """

    # Rule 1: Input must be a string.
    if not isinstance(value, str):
        return False

    # Rule 2: Handle empty string.
    if not value:
        return False

    # Define the Regex components:
    # ^ : Start of string
    # [+-]? : Optional leading plus or minus sign
    # \d+ : One or more digits (integer part)
    # \. : A literal decimal point
    # \d{2} : Exactly two digits (fractional part)
    # $ : End of string
    #
    # Note: We do not allow trailing characters or extra precision.
    # The prompt specifies "precision of 2", implying exactly 2 digits.

    pattern: Final[str] = r"^[+-]?\d+\.\d{2}$"

    # Compile the regex for performance and clarity
    regex_checker = re.compile(pattern)

    # Perform the match
    match_result = regex_checker.match(value)

    # If match_result is None, it didn't meet the criteria
    if match_result is None:
        return False

    return True

# The following logic is provided to ensure the requirements are met.
# Any extra logic or tests are omitted per instructions to return only the block.