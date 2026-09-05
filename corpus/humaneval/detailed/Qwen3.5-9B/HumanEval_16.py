from typing import Set, Dict, Any


def _validate_input(input_value: Any) -> str:
    """
    Validates that the input is a string and not None.
    Raises a ValueError with a descriptive message if validation fails.
    """
    if input_value is None:
        raise ValueError("Input cannot be None; it must be a string instance.")

    if not isinstance(input_value, str):
        raise ValueError(
            f"Input must be a string, but received type: {type(input_value).__name__}."
        )

    return input_value


def _normalize_character(char: str) -> str:
    """
    Converts a single character to lowercase to handle case-insensitivity.
    This ensures 'A' and 'a' are treated as the same character.
    """
    return char.lower()


def _count_distinct_characters_impl(string: str) -> int:
    """
    Core logic to count distinct characters case-insensitively.
    Uses a dictionary to map normalized characters to their first occurrence index
    to ensure uniqueness before counting.

    Args:
        string (str): The validated input string.

    Returns:
        int: The number of distinct characters.
    """
    distinct_characters: Set[str] = set()

    # Edge case: Empty string
    if len(string) == 0:
        return 0

    # Iterate through each character in the string
    for char in string:
        # Normalize the character to lowercase
        normalized_char: str = _normalize_character(char)

        # Add the normalized character to the set (duplicates are automatically ignored)
        distinct_characters.add(normalized_char)

    # Return the count of unique characters found
    return len(distinct_characters)


def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Step 1: Validate the input argument
    validated_string: str = _validate_input(string)

    # Step 2: Execute the core counting logic
    result: int = _count_distinct_characters_impl(validated_string)

    # Step 3: Return the result
    return result