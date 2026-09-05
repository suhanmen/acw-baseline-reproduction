import re
from typing import List

def _validate_input(text: str) -> None:
    """
    Validates the input string.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, got {type(text).__name__}")

def _validate_regex_match_pattern(text: str) -> None:
    """
    Ensures that the internal regex pattern used for this specific problem
    is valid for the given context (Python regex engine).
    This is a defensive check to ensure the pattern compiles.
    """
    # The pattern is constructed inline in the main function, so we check it here
    # to ensure it works as expected for the problem constraints.
    _pattern = r'\b[A-Za-z]{5}\b'
    try:
        re.compile(_pattern)
    except re.error as e:
        raise ValueError(f"Internal regex pattern error: {e}") from e

def _extract_five_letter_words(text: str) -> List[str]:
    """
    Uses a compiled regex pattern to find all substrings that are exactly
    five characters long and consist only of alphabetic characters.

    The pattern breakdown:
    - \b : Word boundary (start)
    - [A-Za-z] : Matches any single alphabetical letter (case-insensitive logic handled by character set)
    - {5} : Matches exactly 5 occurrences of the preceding element
    - \b : Word boundary (end)

    This ensures we don't match parts of longer words (e.g., 'streaming' is not matched).
    """
    # Define the regex pattern
    pattern = r'\b[A-Za-z]{5}\b'

    # Compile the regex for efficiency and clarity, though re.findall handles this too.
    # Using re.UNICODE ensures behavior is consistent across different character sets.
    regex = re.compile(pattern, re.UNICODE)

    # Find all non-overlapping matches in the string
    matches = regex.findall(text)

    return matches

def find_long_word(text: str) -> List[str]:
    """
    Finds all five-character long words in the given string using regex.

    Args:
        text (str): The input string to search within.

    Returns:
        List[str]: A list of strings, each being a word that is exactly 5 characters long.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> find_long_word('Please move back to strem')
        ['strem']
        >>> find_long_word('4K Ultra HD streaming player')
        ['Ultra']
        >>> find_long_word('Streaming Media Player')
        ['Media']
    """
    _validate_input(text)
    _validate_regex_match_pattern(text)

    return _extract_five_letter_words(text)