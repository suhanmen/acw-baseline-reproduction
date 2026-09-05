from typing import List, Union

Number = Union[int, float]

def _validate_input_array(arr: List[Number], name: str = "array") -> None:
    """
    Validates that the provided list is not None and is actually a list.

    Args:
        arr: The list to validate.
        name: The name of the variable to use in error messages.

    Raises:
        TypeError: If arr is not a list.
        ValueError: If arr is empty.
    """
    if arr is None:
        raise ValueError(f"{name} cannot be None.")

    if not isinstance(arr, list):
        raise TypeError(f"{name} must be a list, got {type(arr).__name__}.")

    if len(arr) == 0:
        raise ValueError(f"{name} cannot be empty.")


def _validate_input_array_elements(arr: List[Number]) -> None:
    """
    Validates that all elements in the list are valid numbers (int or float).

    Args:
        arr: The list to validate.

    Raises:
        TypeError: If any element is not a number.
    """
    for index, element in enumerate(arr):
        if not isinstance(element, (int, float)) or (isinstance(element, float) and (element != element)):
            raise TypeError(f"All elements in the array must be numbers (int or float). "
                           f"Invalid element found at index {index}: {element!r} (type: {type(element).__name__}).")


def _find_minimum_value(arr: List[Number]) -> Number:
    """
    Iterates through the array to find the minimum value explicitly.

    Args:
        arr: The validated list of numbers.

    Returns:
        The smallest number found in the list.
    """
    # Initialize current minimum with the first element of the array.
    # Since the array is validated to be non-empty in _validate_input_array,
    # accessing index 0 is safe here.
    current_minimum = arr[0]

    # Iterate starting from the second element.
    for element in arr[1:]:
        # Explicit comparison to update the minimum.
        if element < current_minimum:
            current_minimum = element

    return current_minimum


def _count_occurrences(target_value: Number, arr: List[Number]) -> int:
    """
    Counts how many times a specific value appears in the list.

    Args:
        target_value: The value to count.
        arr: The list in which to count.

    Returns:
        The count of occurrences of target_value in arr.
    """
    occurrence_count = 0

    for element in arr:
        # Explicit equality check using 'is' for identity of singletons is usually fine,
        # but for values from user input or floats, '==' is required for correctness
        # regarding value equality (e.g., 1.0 == 1).
        if element == target_value:
            occurrence_count += 1

    return occurrence_count


def frequency_Of_Smallest(array_size: int, input_array: List[Number]) -> int:
    """
    Finds the frequency of the smallest value in the given array.

    This function performs the following steps:
    1. Validates the input array exists and is not None.
    2. Validates the input is a list.
    3. Validates the input array is not empty.
    4. Validates all elements in the array are valid numbers.
    5. Identifies the smallest value in the array.
    6. Counts the occurrences of that smallest value.
    7. Returns the count.

    Note: The 'array_size' parameter is accepted in the signature for completeness
    but is not used in the logic, as the list length is determined dynamically.
    Using the actual list length ensures robustness against mismatches.

    Args:
        array_size: An integer parameter (reserved for signature compatibility).
        input_array: A list of numbers (int or float).

    Returns:
        An integer representing the frequency of the smallest value.

    Raises:
        TypeError: If input_array is not a list or contains non-numeric elements.
        ValueError: If input_array is empty or None.
    """
    # Step 1 & 2: Validate structure
    _validate_input_array(input_array, "input_array")

    # Step 3: Validate contents (elements)
    _validate_input_array_elements(input_array)

    # Step 4: Find the minimum value
    smallest_value = _find_minimum_value(input_array)

    # Step 5: Count the frequency of the smallest value
    frequency = _count_occurrences(smallest_value, input_array)

    return frequency