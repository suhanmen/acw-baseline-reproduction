from typing import List, Optional

def _validate_input(data: Optional[List[int]], length_hint: int) -> None:
    """
    Validates the input arguments for the re_arrange_array function.

    This function performs several checks:
    1. Ensures 'data' is not None.
    2. Ensures 'data' is a list.
    3. Ensures all elements in 'data' are integers.
    4. Ensures 'length_hint' is a non-negative integer.
    5. Ensures 'length_hint' matches the actual length of 'data'.

    If any validation fails, a ValueError is raised with a descriptive message.
    """
    # Check for None input
    if data is None:
        raise ValueError("Input 'data' cannot be None.")

    # Check if data is a list
    if not isinstance(data, list):
        raise TypeError(f"Input 'data' must be a list, but got {type(data).__name__}.")

    # Validate that length_hint is an integer and non-negative
    if not isinstance(length_hint, int) or isinstance(length_hint, bool):
        raise TypeError(f"Input 'length_hint' must be an integer, but got {type(length_hint).__name__}.")

    if length_hint < 0:
        raise ValueError(f"Input 'length_hint' must be non-negative, but got {length_hint}.")

    # Get the actual length of the data list
    actual_length = len(data)

    # Validate that the length hint matches the actual data length
    if length_hint != actual_length:
        raise ValueError(
            f"Length mismatch: Provided 'length_hint' ({length_hint}) does not match "
            f"the actual length of 'data' ({actual_length})."
        )

    # Iterate through the list to validate each element is an integer
    for index, item in enumerate(data):
        if not isinstance(item, int) or isinstance(item, bool):
            raise TypeError(
                f"Element at index {index} is not an integer (got {type(item).__name__}). "
                f"All elements must be integers."
            )


def _is_negative(number: int) -> bool:
    """
    Helper function to determine if a number is negative.

    Arguments:
    number (int): The integer to check.

    Returns:
    bool: True if number is strictly less than zero, False otherwise.
    """
    return number < 0


def _rearrange_array(data: List[int]) -> List[int]:
    """
    Rearranges the elements of the given list so that all negative elements
    appear before positive (and zero) elements.

    This function creates a new list to store the result, preserving the order
    of elements as they appear in the original list (stable partition).

    Arguments:
    data (List[int]): The list of integers to be rearranged.

    Returns:
    List[int]: A new list with negative numbers followed by non-negative numbers.
    """
    # Initialize two separate lists to hold negative and non-negative numbers
    negative_numbers: List[int] = []
    non_negative_numbers: List[int] = []

    # Iterate through each element in the input list
    for current_element in data:
        # Check if the current element is negative
        if _is_negative(current_element):
            # Append negative numbers to their respective list
            negative_numbers.append(current_element)
        else:
            # Append non-negative numbers (including zero) to their respective list
            non_negative_numbers.append(current_element)

    # Concatenate the two lists to form the final result
    # All negative numbers come first, followed by all non-negative numbers
    rearranged_data = negative_numbers + non_negative_numbers

    return rearranged_data


def re_arrange_array(data: Optional[List[int]], length_hint: int) -> List[int]:
    """
    Rearranges the elements of the given array so that all negative elements 
    appear before positive ones (and zeros).

    This function performs input validation, validates the integrity of the 
    provided length hint, and then uses a stable partitioning approach to 
    reorder the elements.

    Arguments:
    data (List[int]): A list of integers. Can be empty or contain any number 
                      of negative, positive, or zero values.
    length_hint (int): An optional hint for the expected length of 'data'. 
                       This is strictly validated against the actual length.

    Returns:
    List[int]: A new list containing the same elements as 'data', but reordered 
               such that all negative integers appear before all non-negative 
               integers.

    Raises:
    TypeError: If 'data' is not a list or if 'length_hint' is not a valid integer.
    ValueError: If 'data' is None, 'length_hint' is negative, or the provided 
                length hint does not match the actual length of 'data'.
    """
    # Step 1: Validate all inputs explicitly
    _validate_input(data, length_hint)

    # Step 2: Perform the rearrangement logic on the validated data
    # We create a copy inside this function to ensure we return a new list
    # and do not mutate the input list in place, which is safer for functional usage.
    result = _rearrange_array(list(data))

    return result