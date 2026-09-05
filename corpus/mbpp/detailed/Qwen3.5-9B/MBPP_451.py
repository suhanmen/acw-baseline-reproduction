import re
from typing import Optional, Union

InputString = Union[str, None]


def validate_input_string(value: InputString) -> str:
    """
    Validates that the input is a non-None string.
    Raises a TypeError if the input is None or not a string.
    """
    if value is None:
        raise TypeError("Input cannot be None. Expected a string.")
    if not isinstance(value, str):
        raise TypeError(f"Input must be a string, but got {type(value).__name__}.")

    # Ensure the string is not empty if the problem domain implies non-empty input is required,
    # though empty strings are valid strings and will simply return an empty string.
    # We allow empty strings here as they are valid inputs that return empty results.
    return value


def extract_whitespace_pattern() -> str:
    """
    Returns the regular expression pattern for matching any whitespace character.
    \s matches any whitespace character, including space, tab, newline, return, formfeed, etc.
    """
    return r'\s+'


def remove_all_occurrences(input_text: str, pattern: str) -> str:
    """
    Uses re.sub to find all occurrences of the pattern in the input text
    and replaces them with an empty string.

    Args:
        input_text: The text to process.
        pattern: The regex pattern to match.

    Returns:
        The processed text with all matches removed.
    """
    return re.sub(pattern, '', input_text)


def remove_whitespaces(input_string: InputString) -> str:
    """
    Removes all whitespaces from the given string using regex.

    This function handles edge cases explicitly:
    - None input: Raises TypeError.
    - Non-string input: Raises TypeError.
    - Empty string: Returns an empty string.
    - String with no whitespaces: Returns the original string.
    - String with leading/trailing whitespaces: Removes them.
    - String with multiple consecutive whitespaces: Collapses them to nothing.

    Args:
        input_string: The input string potentially containing whitespaces.

    Returns:
        A new string with all whitespace characters removed.

    Raises:
        TypeError: If the input is not a valid string or is None.
    """
    # Step 1: Validate the input
    validated_input = validate_input_string(input_string)

    # Step 2: Define the regex pattern for whitespace
    whitespace_pattern = extract_whitespace_pattern()

    # Step 3: Perform the substitution to remove all whitespace occurrences
    result_string = remove_all_occurrences(validated_input, whitespace_pattern)

    return result_string