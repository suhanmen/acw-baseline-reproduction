from typing import List, Optional

def _validate_input_array(array: List) -> None:
    """
    Validates that the provided array is a list of integers.
    Raises a TypeError if the array is empty or contains non-integer elements.
    """
    if not isinstance(array, list):
        raise TypeError(f"Expected a list, but got {type(array).__name__}")

    if len(array) == 0:
        raise ValueError("The input array cannot be empty.")

    for index, value in enumerate(array):
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"All elements must be integers. Found type {type(value).__name__} at index {index}.")

def _is_sorted_ascending(array: List[int]) -> bool:
    """
    Checks if the array is sorted in non-decreasing (ascending) order.
    The problem description implies a sorted array, but this function
    ensures the precondition is met for the binary search logic to work correctly.
    """
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

def _binary_search_last_occurrence(array: List[int], target: int) -> int:
    """
    Performs a binary search to find the index of the last occurrence of target.
    Assumes the array is sorted in ascending order and has at least one element.

    Returns:
        The index of the last occurrence of target, or -1 if not found.
    """
    left_index: int = 0
    right_index: int = len(array) - 1
    last_found_index: int = -1

    # Standard binary search loop
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = array[middle_index]

        if middle_value == target:
            # We found the target, record this index and continue searching to the right
            last_found_index = middle_index
            left_index = middle_index + 1
        elif middle_value < target:
            # Target must be in the right half
            left_index = middle_index + 1
        else:  # middle_value > target
            # Target must be in the left half
            right_index = middle_index - 1

    return last_found_index

def find_last_occurrence(array: List[int], target: int) -> int:
    """
    Finds the index of the last occurrence of a given number in a sorted array.

    Args:
        array: A list of integers. Must be sorted in ascending order.
        target: The integer number to search for.

    Returns:
        The zero-based index of the last occurrence of the target number.
        Returns -1 if the target is not present in the array.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input array is empty.
        AssertionError: If the input array is not sorted in ascending order.
    """
    # 1. Validate the array structure and contents
    _validate_input_array(array)

    # 2. Validate the sorting precondition explicitly
    if not _is_sorted_ascending(array):
        raise AssertionError("The input array must be sorted in ascending order.")

    # 3. Handle the specific case where the target is not in the array efficiently via binary search
    # Even though we need the last occurrence, binary search is O(log n) which is optimal.
    result_index = _binary_search_last_occurrence(array, target)

    return result_index