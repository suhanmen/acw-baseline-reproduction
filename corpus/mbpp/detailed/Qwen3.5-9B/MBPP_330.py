import re
from typing import List

def find_char(text: str) -> List[str]:
    """
    Finds all words of length 3, 4, or 5 in the given string using regex.

    The function handles:
    - Empty strings
    - Strings with no matching words
    - Strings with mixed case
    - Strings with punctuation adjacent to words (strips non-word characters)
    - Boundary cases like single character strings, all equal lengths, etc.

    Args:
        text (str): The input string to search for words.

    Returns:
        List[str]: A list of words with lengths 3, 4, or 5, preserving original casing.
    """

    # Validate input type
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, got {type(text).__name__}")

    # Handle empty string or None-like empty string
    if not text:
        return []

    # Define the regex pattern for words of length 3, 4, or 5
    # \b word boundary ensures we match whole words
    # [a-zA-Z]{3,5} matches 3 to 5 alphabetic characters
    pattern = r'\b[a-zA-Z]{3,5}\b'

    # Find all matches using the regex pattern
    # re.findall returns a list of strings matching the pattern
    matches = re.findall(pattern, text)

    return matches