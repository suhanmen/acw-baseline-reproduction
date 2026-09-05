from typing import List
from typing import Any


def _is_string_value(value: Any, context_name: str) -> bool:
    """
    Validate that a single value is an instance of str.

    Args:
        value: The value to check.
        context_name: A descriptive name for the variable (used in error message).

    Returns:
        True if the value is a string.

    Raises:
        TypeError: If the value is not a string.
    """
    if not isinstance(value, str):
        raise TypeError(f"Expected {context_name} to be of type 'str', got {type(value).__name__} instead.")
    return True


def _is_string_type(value: Any, context_name: str) -> bool:
    """
    Validate that a value is specifically a string and not a subclass that might behave differently
    (though in Python str is often a base, this ensures strict adherence).

    Args:
        value: The value to check.
        context_name: A descriptive name for the variable.

    Returns:
        True if the value is a str.

    Raises:
        TypeError: If the value is not a str.
    """
    if not isinstance(value, str):
        raise TypeError(f"The input {context_name} is not a valid string object.")
    return True


def _validate_list_type(item: Any, context_name: str) -> None:
    """
    Validate that an element in the list is a string.

    Args:
        item: The item being validated.
        context_name: The name of the input list variable.

    Raises:
        TypeError: If the item is not a string.
    """
    _is_string_value(item, f"element in {context_name}")


def _validate_substring_type(substring: Any, context_name: str) -> None:
    """
    Validate that the substring argument is a string.

    Args:
        substring: The substring to search for.
        context_name: The name of the argument.

    Raises:
        TypeError: If the substring is not a string.
    """
    _is_string_value(substring, context_name)


def _check_contains(string: str, substring: str) -> bool:
    """
    Helper function to determine if a string contains the given substring.

    This is a simple wrapper around the 'in' operator to make the logic explicit.

    Args:
        string: The string to search within.
        substring: The substring to search for.

    Returns:
        True if substring is found in string, False otherwise.
    """
    return substring in string


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Step 1: Validate the 'strings' argument is a list
    if not isinstance(strings, list):
        raise TypeError(f"The argument 'strings' must be a list, got {type(strings).__name__} instead.")

    # Step 2: Validate the 'substring' argument is a string
    _validate_substring_type(substring, "substring")

    # Step 3: Initialize the result list
    filtered_results: List[str] = []

    # Step 4: Iterate over each item in the input list with explicit indexing
    # This ensures we handle the list structure carefully.
    for index in range(len(strings)):
        current_item = strings[index]

        # Step 5: Validate each item in the list is actually a string
        _validate_list_type(current_item, "strings")

        # Step 6: Check if the current string contains the substring
        contains_substring = _check_contains(current_item, substring)

        # Step 7: If it does, add it to the results list
        if contains_substring:
            filtered_results.append(current_item)

    # Step 8: Return the final filtered list
    return filtered_results