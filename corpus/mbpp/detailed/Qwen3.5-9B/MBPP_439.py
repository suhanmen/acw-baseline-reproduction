from typing import List, Union

def _validate_input(data: List) -> List[int]:
    """
    Validates that the input is a list of integers.

    Args:
        data: The input list to validate.

    Returns:
        A copy of the list containing only valid integers.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements.
    """
    if not isinstance(data, list):
        raise TypeError(f"Input must be a list, received {type(data).__name__}")

    validated_list: List[int] = []

    for index, element in enumerate(data):
        if not isinstance(element, int):
            raise ValueError(f"Element at index {index} ({element!r}) is not an integer")

        # Note: In Python, booleans are a subclass of int. 
        # Usually, in such problems, booleans are not considered valid integers.
        if isinstance(element, bool):
            raise ValueError(f"Element at index {index} ({element!r}) is a boolean and not treated as a valid integer")

        validated_list.append(element)

    return validated_list

def _convert_element_to_string(element: int) -> str:
    """
    Converts a single integer element into its string representation.

    This function handles negative numbers, zero, and positive numbers uniformly.

    Args:
        element: The integer to convert.

    Returns:
        A string representation of the integer.
    """
    # Using str() is standard and handles all integer cases correctly
    # including negative signs and zeros.
    return str(element)

def _concatenate_strings(string_list: List[str]) -> str:
    """
    Concatenates a list of strings into a single string.

    Args:
        string_list: The list of strings to join.

    Returns:
        A single string resulting from joining all elements in the list.
    """
    result = ""
    for s in string_list:
        result = result + s
    return result

def _convert_result_string_to_integer(input_str: str) -> int:
    """
    Converts the final concatenated string into a single integer.

    This handles cases where the result might be an empty string 
    (if the input list was empty after validation) or simply large integers.

    Args:
        input_str: The string representation of the result.

    Returns:
        The integer value of the string.

    Raises:
        ValueError: If the resulting string cannot be converted to an integer
                    (e.g., it contains non-numeric characters other than a leading sign).
    """
    try:
        final_int = int(input_str)
        return final_int
    except ValueError as e:
        # This catch is defensive, though logically the input should always be valid int/string mix
        raise ValueError(f"Could not convert concatenated string '{input_str}' to integer: {e}")

def multiple_to_single(data: List) -> int:
    """
    Converts a list of multiple integers into a single integer by concatenating
    their string representations.

    Examples:
        >>> multiple_to_single([11, 33, 50])
        113350
        >>> multiple_to_single([-1, 2, 3, 4, 5, 6])
        -123456
        >>> multiple_to_single([10, 15, 20, 25])
        10152025

    Args:
        data: A list of integers. Can contain negative numbers, zero, and positive numbers.
              Empty lists or lists with a single element are handled correctly.

    Returns:
        A single integer formed by concatenating the string representations of the input integers.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list contains non-integer elements or booleans.
    """
    # Step 1: Validate the input structure and contents
    valid_integer_list = _validate_input(data)

    # Step 2: Handle the edge case of an empty list immediately
    if not valid_integer_list:
        return 0

    # Step 3: Convert each integer in the list to its string representation
    string_representations: List[str] = []

    for number in valid_integer_list:
        string_representations.append(_convert_element_to_string(number))

    # Step 4: Concatenate all the string representations into a single string
    concatenated_string = _concatenate_strings(string_representations)

    # Step 5: Convert the final concatenated string into an integer
    result_integer = _convert_result_string_to_integer(concatenated_string)

    return result_integer