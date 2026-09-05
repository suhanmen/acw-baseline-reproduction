from typing import List, Optional

def _split_into_words(text: str, delimiter: str) -> List[str]:
    """
    Helper function to split a string by a delimiter.

    Args:
        text: The string to split.
        delimiter: The character to use as a delimiter (default is space).

    Returns:
        A list of strings obtained by splitting the input text.

    Raises:
        ValueError: If the input text is not a string or if the delimiter is not a string.
    """
    if not isinstance(text, str):
        raise ValueError(f"Input must be a string, got {type(text).__name__}")
    if not isinstance(delimiter, str):
        raise ValueError(f"Delimiter must be a string, got {type(delimiter).__name__}")

    return text.split(delimiter)

def string_to_list(text: str) -> List[str]:
    """
    Converts a string into a list of words based on spaces.

    This function splits a given input string by spaces and returns a list 
    containing the resulting substrings. It handles various edge cases including 
    empty strings, single words, multiple consecutive spaces, and leading/trailing 
    whitespace.

    Args:
        text (str): The input string to be converted.

    Returns:
        List[str]: A list of strings derived from splitting the input by spaces.

    Raises:
        ValueError: If the input is not a string or is empty (after stripping).
        TypeError: If the input type is unexpected.

    Example:
        >>> string_to_list("hello world")
        ['hello', 'world']

        >>> string_to_list("")
        ValueError: Input string is empty or contains only whitespace.
    """
    # Input validation for type
    if not isinstance(text, str):
        raise TypeError(f"Expected string input, received {type(text).__name__}")

    # Check for empty or whitespace-only string explicitly
    stripped_text = text.strip()
    if not stripped_text:
        raise ValueError("Input string is empty or contains only whitespace.")

    # Check for invalid delimiter if we were to make it configurable (not applicable here, but good practice)
    # For this problem, the delimiter is implicitly a single space ' '.
    delimiter = ' '

    # Perform the split operation
    words_list = _split_into_words(text, delimiter)

    # Additional check: ensure the split didn't produce unexpected empty strings 
    # due to consecutive spaces (though split() handles this by default, we verify logic integrity)
    if any(word == '' for word in words_list):
        raise ValueError("Invalid input string containing consecutive delimiters resulting in empty segments.")

    return words_list