from typing import Any


def _validate_input(input_data: Any) -> None:
    """
    Validates that the input is a string.

    Raises:
        TypeError: If the input is not of type str.
    """
    if not isinstance(input_data, str):
        raise TypeError(f"Input must be a string, but received {type(input_data).__name__}")


def _normalize_to_lowercase(input_string: str) -> str:
    """
    Converts the input string to lowercase to ensure 
    case-insensitivity as per requirements.
    """
    return input_string.lower()


def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Defensive programming: Validate input type immediately
    _validate_input(string)

    # Handle edge case: Empty string
    # An empty string contains 0 distinct characters.
    if not string:
        return 0

    # Step 1: Normalize the string to a uniform case.
    # This ensures 'A' and 'a' are treated as the same character.
    normalized_string: str = _normalize_to_lowercase(string)

    # Step 2: Identify unique characters.
    # Using a set is the most efficient way to extract unique elements.
    # We iterate through the string and add each character to the set.
    unique_chars_collection = set()

    for character in normalized_string:
        unique_chars_collection.add(character)

    # Step 3: Determine the count.
    # The size of the set represents the number of unique characters.
    distinct_count: int = len(unique_chars_collection)

    return distinct_count