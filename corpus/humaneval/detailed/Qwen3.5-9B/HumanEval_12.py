from typing import List, Optional


def _validate_input_strings(strings: List[str]) -> List[str]:
    """
    Validates that the input is indeed a list of strings.

    Args:
        strings: The input list to validate.

    Returns:
        The validated list of strings if successful.

    Raises:
        TypeError: If the input is not a list or if any element is not a string.
    """
    if not isinstance(strings, list):
        raise TypeError(f"Expected a list, but got {type(strings).__name__}")

    for index, item in enumerate(strings):
        if not isinstance(item, str):
            raise TypeError(f"Expected a string at index {index}, but got {type(item).__name__}")

    return strings


def _get_longest_string(strings: List[str]) -> Optional[str]:
    """
    Determines the longest string in the validated list.

    Logic:
    1. If the list is empty, return None.
    2. If the list has one element, return that element.
    3. Iterate through the list to find the maximum length.
    4. In case of ties (multiple strings with the same max length),
       return the first one encountered.

    Args:
        strings: A list of validated strings.

    Returns:
        The longest string, or None if the list is empty.
    """
    # Handle empty list edge case
    if len(strings) == 0:
        return None

    # Handle single element list edge case
    if len(strings) == 1:
        return strings[0]

    # Initialize variables to track the longest string found so far.
    # Using the first element as the initial candidate guarantees we have a valid start.
    current_longest_string: Optional[str] = strings[0]
    max_length: int = len(current_longest_string)

    # Iterate starting from the second element to avoid redundant checks.
    for current_string in strings[1:]:
        current_length: int = len(current_string)

        # Explicit comparison logic to ensure we only update if strictly greater.
        # This satisfies the requirement to return the first one in case of ties.
        if current_length > max_length:
            max_length = current_length
            current_longest_string = current_string

    return current_longest_string


def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    This function performs input validation to ensure type safety before processing.

    Args:
        strings: A list containing string elements.

    Returns:
        The longest string found in the list, or None if the list is empty.

    Raises:
        TypeError: If the input is not a list or contains non-string elements.

    Examples:
        >>> longest([])
        None
        >>> longest(['a', 'b', 'c'])
        'a'
        >>> longest(['a', 'bb', 'ccc'])
        'ccc'
        >>> longest(['short', 'shorter', 'shortest'])
        'shortest'
        >>> longest(['x', 'xx', 'xxx', 'xxx'])
        'xxx'
    """
    # Step 1: Validate inputs and raise explicit errors for invalid types.
    validated_strings: List[str] = _validate_input_strings(strings)

    # Step 2: Compute the longest string using the helper function.
    result: Optional[str] = _get_longest_string(validated_strings)

    # Step 3: Return the result.
    return result