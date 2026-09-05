import re
from typing import List, Union

def _is_digit_sequence_char(character: str) -> bool:
    """
    Checks if a single character is a digit (0-9).

    Args:
        character: A single string character to check.

    Returns:
        True if the character is a digit, False otherwise.
    """
    if not isinstance(character, str):
        raise TypeError(f"Expected a string character, got {type(character).__name__}")

    if len(character) != 1:
        raise ValueError(f"Expected a single character string, got string of length {len(character)}")

    return character.isdigit()


def _sanitize_string(input_string: str) -> str:
    """
    Validates the input string and returns it if valid.

    This function serves as an explicit validation step before processing.

    Args:
        input_string: The string to validate.

    Returns:
        The validated string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected a string, got {type(input_string).__name__}")

    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty.")

    return input_string


def _remove_digits_from_string(input_string: str) -> str:
    """
    Removes all digit characters from the given string.

    This function iterates through each character of the string,
    explicitly checks if it is a digit using our helper function,
    and builds a new string containing only non-digit characters.

    Args:
        input_string: The string from which digits should be removed.

    Returns:
        A new string with all digit characters removed.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    # Validate input explicitly
    validated_string = _sanitize_string(input_string)

    if len(validated_string) == 0:
        return ""

    # Initialize result list for explicit character-by-character construction
    result_characters: List[str] = []

    # Iterate over each character explicitly
    current_index: int = 0
    while current_index < len(validated_string):
        current_char: str = validated_string[current_index]

        # Check if the character is a digit using our explicit helper
        is_digit: bool = _is_digit_sequence_char(current_char)

        # Append only if it is not a digit
        if not is_digit:
            result_characters.append(current_char)

        # Move to the next character
        current_index += 1

    # Join the list of characters back into a string
    final_string: str = "".join(result_characters)

    return final_string


def remove(input_list: Union[List[str], None]) -> List[str]:
    """
    Removes all digits from a list of strings.

    This function processes a list of strings, sanitizing each one,
    removing all digit characters, and returning a new list with
    the processed strings.

    Args:
        input_list: A list of strings to process.

    Returns:
        A new list of strings with all digits removed from each element.

    Raises:
        TypeError: 
            - If input_list is None.
            - If any element in the list is not a string.
        ValueError: 
            - If input_list is empty.
            - If any string element is empty.
    """
    # Validate the main input list for existence
    if input_list is None:
        raise TypeError("Input list cannot be None.")

    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list, got {type(input_list).__name__}")

    # Validate the main input list for emptiness (degenerate case)
    if len(input_list) == 0:
        raise ValueError("Input list cannot be empty.")

    # Validate that all elements are strings
    for index, item in enumerate(input_list):
        if not isinstance(item, str):
            raise TypeError(f"Element at index {index} is not a string. It is {type(item).__name__}.")

    # Process each string in the list
    processed_list: List[str] = []

    for item in input_list:
        # Sanitize and process the individual string
        processed_item: str = _remove_digits_from_string(item)

        # Add the processed string to the result list
        processed_list.append(processed_item)

    return processed_list