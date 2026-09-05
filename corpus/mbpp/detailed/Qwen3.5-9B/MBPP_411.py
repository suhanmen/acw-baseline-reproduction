import re
from typing import Optional

def _validate_input_string(input_string: str) -> str:
    """
    Validates that the input is a string.
    Raises a TypeError if the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError(
            f"Input must be a string, but got {type(input_string).__name__}"
        )
    return input_string

def _convert_snake_to_camel_case(input_string: str) -> str:
    """
    Converts a snake_case string to camelCase.

    Logic:
    1. The first word remains entirely in lowercase (or rather, starts with lowercase),
       BUT the assertions provided in the problem (e.g., 'AndroidTv') indicate that
       the first letter of the resulting string should be UPPERCASE (Title case for the first part).

    Observation of required behavior:
    'android_tv' -> 'AndroidTv'
    'google_pixel' -> 'GooglePixel'

    Pattern deduction:
    - Split by '_'.
    - First element: Capitalize the first letter, make the rest lowercase.
    - Subsequent elements: Capitalize the first letter, make the rest lowercase, and concatenate.

    However, standard camelCase usually keeps the first word lowercase (e.g., 'androidTv').
    PascalCase (or UpperCamelCase) capitalizes the first letter of every word.
    The provided examples clearly show PascalCase behavior: 'AndroidTv', 'GooglePixel'.
    Therefore, we will treat this requirement as converting to PascalCase style.
    """

    # Split the string by the underscore delimiter
    word_parts = input_string.split('_')

    # If the string is empty, return an empty string
    if not word_parts:
        return ""

    # Process the first word
    # 1. Lowercase the entire first word to handle accidental internal caps or extra caps
    # 2. Capitalize the first character
    first_word_processed = word_parts[0].lower().capitalize()

    # Process the remaining words
    subsequent_words_processed = []

    for word in word_parts[1:]:
        if not word:
            # Skip empty parts resulting from consecutive underscores or trailing/leading underscores
            continue

        # Lowercase the word
        word_lower = word.lower()

        # Capitalize the first letter
        word_camelized = word_lower.capitalize()

        subsequent_words_processed.append(word_camelized)

    # Join the first processed word with the subsequent processed words
    result = first_word_processed + "".join(subsequent_words_processed)

    return result

def snake_to_camel(input_string: str) -> str:
    """
    Converts a snake_case string to a camelCase (specifically PascalCase based on provided examples) string.

    Examples:
    'android_tv' -> 'AndroidTv'
    'google_pixel' -> 'GooglePixel'
    'apple_watch' -> 'AppleWatch'

    Args:
        input_string (str): The snake_case string to convert.

    Returns:
        str: The converted string in PascalCase.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate the input explicitly
    validated_string = _validate_input_string(input_string)

    # Perform the conversion
    return _convert_snake_to_camel_case(validated_string)