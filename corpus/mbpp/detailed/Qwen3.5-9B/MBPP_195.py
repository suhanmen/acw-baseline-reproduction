from typing import List, Tuple, Any, Optional

def is_sorted_ascending(array: List[Any], tolerance: float = 0.0) -> bool:
    """
    Verify if a list is sorted in ascending order.

    Args:
        array: The list to check.
        tolerance: Floating point tolerance for comparison if needed (default 0.0).

    Returns:
        True if the list is sorted in ascending order, False otherwise.
    """
    if not array:
        return True  # An empty list is considered sorted

    for index in range(len(array) - 1):
        current_value = array[index]
        next_value = array[index + 1]

        # Handle potential numeric comparison with tolerance if applicable
        if isinstance(current_value, (int, float)) and isinstance(next_value, (int, float)):
            if next_value < current_value - tolerance:
                return False
        else:
            if next_value < current_value:
                return False

    return True


def find_first_position(array: List[Any], target: Any, max_index: int) -> int:
    """
    Find the first position of an element in a sorted array using binary search.

    This function assumes the input array is sorted in ascending order.
    It searches for the 'target' value and returns the index of its first occurrence.

    Args:
        array: A list of elements sorted in ascending order.
        target: The element to search for.
        max_index: The upper bound index (inclusive) to consider for the search.
                   This allows handling cases where the search space is restricted
                   or the input might be logically truncated.

    Returns:
        The index of the first occurrence of 'target' in 'array' within the range [0, max_index].
        Returns -1 if the target is not found.

    Raises:
        TypeError: If 'array' is not a list, or 'target'/'max_index' are of incorrect types.
        ValueError: If 'array' contains non-comparable elements or is not sorted.
    """
    # --- Input Validation ---

    # Validate array type
    if not isinstance(array, list):
        raise TypeError(f"Expected 'array' to be a list, got {type(array).__name__}")

    # Validate target type
    if target is None:
        raise TypeError("Target cannot be None for comparison logic in this context.")

    # Validate max_index type
    if not isinstance(max_index, int):
        raise TypeError(f"Expected 'max_index' to be an integer, got {type(max_index).__name__}")

    # Validate index range
    array_length = len(array)
    if max_index < 0 or max_index >= array_length:
        raise ValueError(
            f"Invalid 'max_index' ({max_index}). It must be between 0 and {array_length - 1} inclusive."
        )

    # Validate array contents (comparability and sorting)
    # We perform a quick check for sorting consistency
    if not is_sorted_ascending(array):
        raise ValueError("The input array must be sorted in ascending order.")

    # --- Edge Cases Handling ---

    # Handle empty array or trivial range
    if array_length == 0:
        return -1

    # Define the effective search range [low, high]
    low = 0
    high = max_index

    # Initialize result tracker
    first_occurrence_index = -1

    # Binary Search Algorithm
    while low <= high:
        # Calculate mid point to avoid potential infinite loops with floating point arithmetic
        mid = (low + high) // 2

        current_value = array[mid]

        if current_value == target:
            # Found the target, but it might not be the first occurrence.
            # Record this index and continue searching in the left half.
            first_occurrence_index = mid
            high = mid - 1

        elif current_value < target:
            # Target is in the right half
            low = mid + 1

        else:  # current_value > target
            # Target is in the left half
            high = mid - 1

    return first_occurrence_index


def first(array: List[Any], target: Any, max_index: int) -> int:
    """
    Public interface to find the first position of an element in a sorted array.

    This function wraps 'find_first_position' to provide a clean API.
    It enforces the constraints specified in the problem description.

    Args:
        array: A list of elements sorted in ascending order.
        target: The element to search for.
        max_index: The index up to which the search is valid.
                   Based on the provided examples, this seems to represent the 
                   last valid index to check or the length minus one.

    Returns:
        The index of the first occurrence of 'target'.

    Raises:
        TypeError: If inputs are not of the expected types.
        ValueError: If the array is not sorted or indices are invalid.
    """
    if not isinstance(array, list):
        raise TypeError("Input 'array' must be a list.")

    if not isinstance(target, (int, float, str)):
        raise TypeError("Input 'target' must be comparable (int, float, or str).")

    if not isinstance(max_index, int):
        raise TypeError("Input 'max_index' must be an integer.")

    # Check if array is empty
    if len(array) == 0:
        raise ValueError("Input 'array' cannot be empty.")

    # Ensure max_index is within valid bounds [0, len(array) - 1]
    array_length = len(array)
    if max_index < 0 or max_index >= array_length:
        raise ValueError(
            f"max_index ({max_index}) is out of bounds for array of length {array_length}."
        )

    # Ensure the array is actually sorted before proceeding
    if not is_sorted_ascending(array):
        raise ValueError("The provided array is not sorted in ascending order.")

    return find_first_position(array, target, max_index)