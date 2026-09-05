from typing import Tuple, Union
import copy

Number = Union[int, float]

def _validate_input_numbers(values: Tuple[Number, ...]) -> None:
    """
    Validates that all elements in the input tuple are valid numbers (int or float).
    Raises a TypeError if any element is not a valid number.
    """
    for index, value in enumerate(values):
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"All elements in the input tuple must be numbers (int or float). "
                f"Invalid type found at index {index}: {type(value).__name__}"
            )
        # Explicitly check for booleans, as bool is a subclass of int in Python
        # and passing True/False might be considered invalid depending on strictness.
        # Given the problem context usually implies numeric data, we flag booleans.
        if isinstance(value, bool):
            raise TypeError(
                f"All elements in the input tuple must be numeric types (int or float), "
                f"not boolean. Boolean values found at index {index}."
            )

def _validate_input_k(values: Tuple[Number, ...], k: int) -> None:
    """
    Validates that k is a valid non-negative integer.
    Raises a ValueError if k is invalid.
    """
    if not isinstance(k, int):
        raise TypeError(
            f"The parameter 'k' must be an integer, got {type(k).__name__}."
        )
    if k < 0:
        raise ValueError(
            f"The parameter 'k' must be non-negative, got {k}."
        )

def _get_sorted_list_from_tuple(values: Tuple[Number, ...]) -> list:
    """
    Converts the input tuple to a list and sorts it in ascending order.
    Returns the sorted list.
    """
    # Create a copy to avoid modifying the original tuple's conceptual order
    # (though tuples are immutable, we need a list for sorting).
    sorted_list = list(values)
    # Perform the sort explicitly.
    sorted_list.sort()
    return sorted_list

def _select_k_elements(sorted_list: list, k: int) -> Tuple[Number, ...]:
    """
    Extracts the smallest k elements from the sorted list and wraps them in a tuple.
    If k is 0, returns an empty tuple.
    If k is greater than or equal to the list length, returns the entire list as a tuple.
    """
    total_length = len(sorted_list)

    if k == 0:
        return ()

    if k >= total_length:
        # If we need more than available, return all elements.
        return tuple(sorted_list)

    # Slice the list to get the first k elements.
    k_elements = sorted_list[:k]
    return tuple(k_elements)

def extract_min_max(values: Tuple[Number, ...], k: int) -> Tuple[Number, ...]:
    """
    Extracts the minimum and maximum k elements from the given tuple.

    The function interprets "maximum and minimum k elements" based on the provided assertions:
    - It sorts the input tuple in ascending order.
    - It returns a tuple containing the smallest k elements and the largest k elements.
    - If the total number of elements is less than 2*k, it returns all elements.
    - If k is 0, it returns an empty tuple.

    Parameters:
        values (Tuple[Number, ...]): A tuple of numeric values.
        k (int): The number of minimum and maximum elements to extract.

    Returns:
        Tuple[Number, ...]: A tuple containing the sorted minimum k elements followed by the sorted maximum k elements.

    Raises:
        TypeError: If 'values' contains non-numeric types or 'k' is not an integer.
        ValueError: If 'k' is negative.
    """
    # Step 1: Validate the types and content of the input tuple and the integer k.
    _validate_input_numbers(values)
    _validate_input_k(values, k)

    # Step 2: Handle the edge case where k is 0.
    if k == 0:
        return ()

    # Step 3: Handle the edge case where the input tuple is empty.
    # The validation functions above will pass, but logical flow requires care.
    if len(values) == 0:
        return ()

    # Step 4: Sort the values to easily identify min and max segments.
    # We create a new sorted list without modifying any conceptual state of the original.
    sorted_values = _get_sorted_list_from_tuple(values)

    total_count = len(sorted_values)
    required_count = 2 * k

    # Step 5: Determine the slice bounds based on the total count vs required count.
    # Case A: Total elements are less than or equal to 2*k.
    # We return the entire sorted list as the result.
    if total_count <= required_count:
        result_elements = sorted_values
    else:
        # Case B: We have enough elements.
        # Take the first k elements (min).
        min_segment = sorted_values[:k]
        # Take the last k elements (max).
        # In a 0-indexed list of length N, the last k elements start at index N-k.
        max_start_index = total_count - k
        max_segment = sorted_values[max_start_index:]

        # Combine the segments: min elements first, then max elements.
        result_elements = min_segment + max_segment

    # Step 6: Convert the combined list back to a tuple for the return type.
    return tuple(result_elements)