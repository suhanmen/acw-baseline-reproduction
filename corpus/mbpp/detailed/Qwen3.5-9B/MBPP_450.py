from typing import List, Optional, Union

def _validate_size(size: int) -> int:
    """
    Validates that the provided size is a non-negative integer.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.

    Returns:
        The validated size value.
    """
    if not isinstance(size, int):
        raise TypeError(f"Expected an integer for 'size', but got {type(size).__name__}.")

    if size < 0:
        raise ValueError(f"Expected a non-negative integer for 'size', but got {size}.")

    return size

def _validate_strings(values: List[Union[str, None]]) -> List[str]:
    """
    Validates that the input list contains only non-null string elements.

    Raises:
        TypeError: If the input is not a list or if any element is not a string.
        ValueError: If any element in the list is None.

    Returns:
        The validated list of strings.
    """
    if not isinstance(values, list):
        raise TypeError(f"Expected a list for 'values', but got {type(values).__name__}.")

    for index, item in enumerate(values):
        if item is None:
            raise ValueError(f"Found a None value at index {index} in the input list.")
        if not isinstance(item, str):
            raise TypeError(f"Found a non-string value '{type(item).__name__}' at index {index} in the input list.")

    return values

def _filter_strings_by_length(valid_values: List[str], target_size: int) -> List[str]:
    """
    Filters the list of strings to include only those with a length equal to target_size.

    Args:
        valid_values: A list of validated strings.
        target_size: The desired length of the strings.

    Returns:
        A new list containing only the strings that match the target size.
    """
    result = []
    for current_string in valid_values:
        current_length = len(current_string)
        if current_length == target_size:
            result.append(current_string)

    return result

def extract_string(values: List[Union[str, None]], size: int) -> List[str]:
    """
    Extracts strings from a given list that have a specific length.

    This function performs rigorous validation on both the input list and the size parameter.
    It handles edge cases such as empty lists, lists with None values, non-string elements,
    and invalid size values (negative or non-integer).

    Args:
        values: A list of string values to be processed.
        size: An integer representing the desired length of the strings.

    Returns:
        A list of strings from the input that have a length equal to 'size'.

    Raises:
        TypeError: If 'values' is not a list or if 'size' is not an integer.
        ValueError: If 'size' is negative or if any element in 'values' is None.
    """
    # Step 1: Validate the size parameter explicitly before any other processing
    validated_size = _validate_size(size)

    # Step 2: Validate the input list of strings explicitly
    validated_values = _validate_strings(values)

    # Step 3: Filter the validated strings based on the validated size
    filtered_result = _filter_strings_by_length(validated_values, validated_size)

    # Step 4: Return the final filtered list
    return filtered_result