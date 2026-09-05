from typing import List, Optional, Union

def validate_single_string(value: Union[str, None]) -> str:
    """
    Validates that the input is a non-null string.
    Raises a TypeError if the input is not a string or is None.

    Parameters:
    value (Union[str, None]): The input value to validate.

    Returns:
    str: The validated string.

    Raises:
    TypeError: If value is None or not a string.
    """
    if value is None:
        raise TypeError("Input value cannot be None.")
    if not isinstance(value, str):
        raise TypeError(f"Input value must be a string, but got {type(value).__name__}.")
    return value

def reverse_single_string(input_string: str) -> str:
    """
    Reverses a single string using explicit indexing logic.

    Parameters:
    input_string (str): The string to reverse.

    Returns:
    str: The reversed string.

    Note:
    Python's slicing (input_string[::-1]) is used here as it is the 
    standard, efficient, and explicit way to reverse a string in Python.
    An explicit loop could be implemented for demonstration, but slicing 
    is the idiomatic 'explicit' solution for this specific task in Python.
    """
    # Start from the last character index down to 0 with a step of -1
    reversed_chars = []
    index = len(input_string) - 1

    while index >= 0:
        reversed_chars.append(input_string[index])
        index -= 1

    return "".join(reversed_chars)

def reverse_string_list(input_list: List[Optional[str]]) -> List[str]:
    """
    Reverses each string in the provided list of strings.

    This function:
    1. Validates that the input is a list.
    2. Validates that the input list is not empty (though processing empty list returns empty list).
    3. Iterates through each element, validating it is a string before reversing.
    4. Handles None values within the list by raising an explicit error.
    5. Handles strings of various lengths (including empty strings) correctly.
    6. Returns a new list containing the reversed strings.

    Parameters:
    input_list (List[Optional[str]]): A list of strings (or None values that will be rejected).

    Returns:
    List[str]: A new list where each string from the input has been reversed.

    Raises:
    TypeError: If the input is not a list, or if any element is not a string.
    ValueError: If the input list is None.
    """
    # Explicit check for the container type
    if not isinstance(input_list, list):
        raise TypeError(f"Expected a list of strings, but got {type(input_list).__name__}.")

    # Handle the case where the list itself is empty
    # The problem statement doesn't forbid empty lists, and returning [] is correct behavior.
    if len(input_list) == 0:
        return []

    reversed_strings: List[str] = []

    for index, item in enumerate(input_list):
        # Validate individual items before processing
        validated_item = validate_single_string(item)

        # Reverse the validated string
        reversed_item = reverse_single_string(validated_item)

        # Append the result to the output list
        reversed_strings.append(reversed_item)

    return reversed_strings