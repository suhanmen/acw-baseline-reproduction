import re
from typing import Union


def _is_uppercase_vowel(char: str) -> bool:
    """
    Determine if the given character is an uppercase vowel.

    Uppercase vowels are: A, E, I, O, U.
    This function returns True only if the character is exactly one of these.

    :param char: A single character string to check.
    :return: True if uppercase vowel, False otherwise.
    """
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("Input must be a single character string.")

    upper_vowels = {'A', 'E', 'I', 'O', 'U'}
    return char in upper_vowels


def _is_valid_string_input(s: object) -> str:
    """
    Validate that the input is a string and handle None specifically.

    :param s: The input object to validate.
    :return: The validated string.
    :raises TypeError: If input is not a string.
    :raises ValueError: If input is None.
    """
    if s is None:
        raise ValueError("Input cannot be None.")

    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, got {type(s).__name__}.")

    return s


def _count_uppercase_vowels_in_even_indices(s: str) -> int:
    """
    Count the number of uppercase vowels located at even indices in the string.

    Algorithm:
    1. Initialize a counter to zero.
    2. Iterate through the string with index and character.
    3. Check if the index is even (index % 2 == 0).
    4. If even, check if the character is an uppercase vowel.
    5. If both conditions are met, increment the counter.
    6. Return the final count.

    :param s: A validated string to process.
    :return: The count of uppercase vowels at even indices.
    """
    count = 0

    for index, character in enumerate(s):
        is_even_index = (index % 2 == 0)

        if is_even_index:
            if _is_uppercase_vowel(character):
                count += 1

    return count


def count_upper(s: object) -> int:
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0

    Validation:
    - If input is None, raises ValueError.
    - If input is not a string, raises TypeError.

    :param s: The input string to analyze.
    :return: An integer representing the count of uppercase vowels at even indices.
    :raises TypeError: If s is not a string.
    :raises ValueError: If s is None.
    """
    validated_string = _is_valid_string_input(s)
    result = _count_uppercase_vowels_in_even_indices(validated_string)
    return result