from typing import Tuple, Any, Union

def _is_nested_element(element: Any) -> bool:
    """
    Determines if a given element is a tuple (nested structure).

    Args:
        element: The element to check.

    Returns:
        True if the element is a tuple, False otherwise.
    """
    return isinstance(element, tuple)


def _validate_input(input_data: Any) -> Tuple[bool, str]:
    """
    Validates the input data to ensure it meets the requirements.

    Args:
        input_data: The input data to validate.

    Returns:
        A tuple of (is_valid, error_message).
        is_valid is True if the input is valid, False otherwise.
        error_message contains details about the error if the input is invalid.
    """
    if input_data is None:
        return False, "Input data cannot be None."

    if not isinstance(input_data, tuple):
        return False, f"Input data must be a tuple, but got {type(input_data).__name__}."

    if len(input_data) == 0:
        return False, "Input tuple cannot be empty."

    # Validate all elements in the tuple
    for index, element in enumerate(input_data):
        if not isinstance(element, (int, float, tuple)):
            return False, f"Element at index {index} must be an int, float, or tuple, but got {type(element).__name__}."

    return True, ""


def _count_nested_tuples(nested_data: Tuple, current_index: int = 0) -> int:
    """
    Recursively counts the number of nested tuples before the first found nested tuple.

    Args:
        nested_data: The original tuple to search through.
        current_index: The current index being processed (used for recursion tracking).

    Returns:
        The count of elements before the first nested tuple.
    """
    # Base case: If we have processed all elements without finding a nested tuple
    if current_index >= len(nested_data):
        return 0

    current_element = nested_data[current_index]

    if _is_nested_element(current_element):
        # Found the first nested tuple
        return current_index

    # Move to the next element
    return _count_nested_tuples(nested_data, current_index + 1)


def count_first_elements(input_tuple: Tuple) -> int:
    """
    Finds the element count that occurs before the record (nested tuple) in the given tuple.

    This function searches for the first occurrence of a nested tuple within the provided
    tuple and returns the count of elements that appear before it.

    Args:
        input_tuple: A tuple containing elements which can be integers, floats, or other tuples.

    Returns:
        An integer representing the count of elements before the first nested tuple.

    Raises:
        ValueError: If the input validation fails (empty tuple, invalid types, etc.).
    """
    # Step 1: Validate the input data
    is_valid, error_message = _validate_input(input_tuple)

    if not is_valid:
        raise ValueError(error_message)

    # Step 2: Count the elements before the first nested tuple
    count_before_record = _count_nested_tuples(input_tuple)

    # Step 3: Return the result
    return count_before_record