import math

def _validate_input(arr):
    """
    Validates that the input is a list (or array-like sequence) of integers.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError(f"Input must be a list, but got {type(arr).__name__}")

    # Check for empty list (which is valid, will be handled in main logic, but good to note)
    if len(arr) == 0:
        return

    # Validate each element is an integer (bool is a subclass of int in Python, so we exclude it explicitly)
    for index, element in enumerate(arr):
        if isinstance(element, bool) or not isinstance(element, int):
            raise ValueError(f"All elements must be integers. Element at index {index} is {type(element).__name__}: {element}")

def _calculate_mismatch_count(arr):
    """
    Calculates the minimum number of changes required to make the array palindromic.

    The strategy is to compare elements from the start and end moving inwards.
    For every pair (arr[i], arr[n-1-i]), if they are not equal, we need exactly one change
    to make them equal (change one to match the other).

    Returns:
        int: The count of mismatches.
    """
    length = len(arr)

    # If length is 0 or 1, it's already a palindrome, so 0 changes needed.
    if length <= 1:
        return 0

    changes_needed = 0
    half_length = length // 2
    left_index = 0
    right_index = length - 1

    # Iterate through the first half of the array
    while left_index < right_index:
        current_left_value = arr[left_index]
        current_right_value = arr[right_index]

        # Compare the mirrored elements
        if current_left_value != current_right_value:
            # Increment change counter if they don't match
            changes_needed = changes_needed + 1

        # Move pointers inward
        left_index = left_index + 1
        right_index = right_index - 1

    return changes_needed

def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """

    # Step 1: Validate the input to ensure type safety and integrity
    _validate_input(arr)

    # Step 2: Delegate the calculation logic to the helper function
    result = _calculate_mismatch_count(arr)

    # Step 3: Return the computed result
    return result