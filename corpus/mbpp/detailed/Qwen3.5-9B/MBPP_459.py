import re
from typing import Union

def remove_uppercase(text: str) -> str:
    """
    Removes all uppercase substrings from the given input string using regex.

    This function uses a regular expression to identify and remove all contiguous
    sequences of uppercase letters within the input string. It handles various edge
    cases including empty strings, single characters, strings with no uppercase,
    strings with all uppercase, and strings with mixed or no content.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with all uppercase substrings removed.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string contains null characters or other invalid data (though regex handles most, this validates intent).
    """
    # Validate input type
    if not isinstance(text, str):
        raise TypeError(f"Expected input of type 'str', but received '{type(text).__name__}'.")

    # Define a regular expression pattern that matches one or more consecutive uppercase letters.
    # \p{L} isn't standard in Python's re module without regex flag support for specific scripts usually,
    # but for standard ASCII/A-Z we use [A-Z]+. The problem examples imply standard alphabets.
    uppercase_pattern = r'[A-Z]+'

    # Validate that the pattern was defined correctly (basic sanity check)
    if not uppercase_pattern or not isinstance(uppercase_pattern, str):
        raise ValueError("Internal error: Regex pattern definition failed.")

    # Perform the substitution: replace all matches of the pattern with an empty string.
    # The re.sub function returns a new string with the replacements made.
    cleaned_text = re.sub(uppercase_pattern, '', text)

    # Return the resulting string.
    return cleaned_text