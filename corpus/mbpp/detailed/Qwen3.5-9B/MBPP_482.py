import re
from typing import Tuple, Optional

def _validate_input(input_string: str) -> str:
    """
    Validates that the input is a string and raises a TypeError if it is not.
    Returns the validated string.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string input, but received {type(input_string).__name__}")
    return input_string

def _find_pattern_match(input_string: str) -> Optional[re.Match]:
    """
    Uses regex to find a sequence of exactly one upper case letter followed
    by zero or more lower case letters in the given string.
    Returns a Match object if found, otherwise None.

    Pattern breakdown:
    ^[A-Z][a-z]*$ - This is a stricter interpretation for single token matching,
    but the problem asks to find sequences IN the string.

    However, looking at the assertions:
    1. "Geeks" -> 'Yes' (G followed by eeks)
    2. "geeksforGeeks" -> 'Yes' (Geeks at the end matches)
    3. "geeks" -> 'No' (starts with lower, no upper case start sequence)

    The regex used will be: [A-Z][a-z]*
    We need to find IF this pattern exists anywhere in the string.
    """
    # Define the regex pattern:
    # [A-Z]  : Matches exactly one upper case letter.
    # [a-z]* : Matches zero or more lower case letters.
    pattern = r"[A-Z][a-z]*"

    # Perform the search. search() finds the first location where the regex produces a match.
    match_result = re.search(pattern, input_string)

    return match_result

def match(input_string: str) -> str:
    """
    Finds sequences of one upper case letter followed by lower case letters
    in the given string using regex.

    Returns:
        'Yes' if a valid sequence is found.
        'No' if no valid sequence is found.

    Raises:
        TypeError: If the input is not a string.
    """
    # Step 1: Validate the input to ensure it is a string.
    validated_string = _validate_input(input_string)

    # Step 2: Attempt to find the pattern in the validated string.
    found_match = _find_pattern_match(validated_string)

    # Step 3: Determine the result based on whether a match was found.
    # If found_match is not None, it means the pattern exists, so return 'Yes'.
    if found_match is not None:
        result = 'Yes'
    else:
        result = 'No'

    return result