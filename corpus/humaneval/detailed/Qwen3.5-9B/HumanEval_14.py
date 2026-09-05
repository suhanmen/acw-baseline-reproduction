from typing import List


def _validate_input_string(input_string: str) -> None:
    """
    Validates that the input is indeed a string.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(input_string, str):
        raise TypeError(
            f"Expected a string, but got {type(input_string).__name__} instead."
        )


def _generate_prefixes(string_value: str) -> List[str]:
    """
    Generates all prefixes of the given string, from shortest to longest.

    Args:
        string_value (str): The string to generate prefixes for.

    Returns:
        List[str]: A list of all prefixes, starting with the first character
                   up to the entire string.
    """
    prefixes_list: List[str] = []

    # Handle the empty string edge case explicitly.
    # An empty string has no prefixes (the list remains empty).
    if string_value == "":
        return prefixes_list

    # Iterate through the string, using index i from 0 to len(string_value)-1.
    # At each step i, we take the slice from the start (0) up to i+1 (exclusive).
    # This creates substrings of length 1, 2, 3, ..., n.
    for current_index in range(len(string_value)):
        current_prefix = string_value[0 : current_index + 1]
        prefixes_list.append(current_prefix)

    return prefixes_list


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    >>> all_prefixes('')
    []
    >>> all_prefixes('a')
    ['a']
    >>> all_prefixes('aaaa')
    ['a', 'aa', 'aaa', 'aaaa']
    """
    # Step 1: Validate the input type strictly.
    # This ensures defensive programming against non-string inputs like None, 
    # integers, or lists which might behave unexpectedly in a loop.
    _validate_input_string(string)

    # Step 2: Generate and return the prefixes.
    # We delegate the logic to a separate helper function for clarity and 
    # to isolate the slicing logic from validation logic.
    result_list = _generate_prefixes(string)

    return result_list