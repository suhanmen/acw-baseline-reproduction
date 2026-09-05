from typing import List, Optional

def _validate_input_list(values: object) -> Optional[List[str]]:
    """
    Validates that the input is a list of strings.
    Returns the validated list or raises a TypeError if invalid.
    """
    if not isinstance(values, list):
        raise TypeError(f"Expected a list of strings, but got {type(values).__name__}")

    for index, item in enumerate(values):
        if not isinstance(item, str):
            raise TypeError(
                f"Expected all items to be strings, but found item at index {index} "
                f"of type {type(item).__name__} with value '{item}'"
            )

    return values

def _validate_search_string(substring: object) -> str:
    """
    Validates that the input substring is a string.
    Returns the validated string or raises a TypeError if invalid.
    """
    if not isinstance(substring, str):
        raise TypeError(
            f"Expected a string for the substring, but got {type(substring).__name__}"
        )

    return substring

def _find_substring_in_list(valid_list: List[str], search_string: str) -> bool:
    """
    Iterates through the list and checks if the search_string 
    is present within any of the string elements.

    Args:
        valid_list: A list of validated strings.
        search_string: The string to search for.

    Returns:
        True if the substring is found, False otherwise.
    """
    # Check for empty list edge case explicitly
    if len(valid_list) == 0:
        return False

    # Iterate through each element in the list
    for element in valid_list:
        # Check if the current element contains the substring
        if search_string in element:
            return True

    # If no element contained the substring after checking all
    return False

def find_substring(values: List[str], substring: str) -> bool:
    """
    Checks if a substring is present in any of the strings within the given list.

    This function performs rigorous input validation before proceeding with the search.
    It handles edge cases such as empty lists, single-element lists, and lists with
    elements containing the search string multiple times or at boundaries.

    Args:
        values: A list of string values to search within.
        substring: The string sequence to look for.

    Returns:
        bool: True if the substring is found in any element of the list, False otherwise.

    Raises:
        TypeError: If 'values' is not a list or if 'substring' is not a string,
                   or if any element within 'values' is not a string.
    """
    # Step 1: Validate the list of values
    validated_list = _validate_input_list(values)

    # Step 2: Validate the search substring
    validated_substring = _validate_search_string(substring)

    # Step 3: Perform the search using the explicit helper function
    result = _find_substring_in_list(validated_list, validated_substring)

    return result