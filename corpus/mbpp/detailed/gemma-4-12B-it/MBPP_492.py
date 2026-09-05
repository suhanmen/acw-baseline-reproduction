from typing import List, Any, Union

def binary_search(arr: List[Union[int, float]], target: Union[int, float]) -> bool:
    """
    Performs a binary search to determine if a target element exists in a 
    sorted list of numbers.

    Args:
        arr: A sorted list of integers or floats.
        target: The value to search for.

    Returns:
        bool: True if target is found, False otherwise.

    Raises:
        TypeError: If input types are not list or numeric.
        ValueError: If the input list is not sorted.
    """

    # --- Input Validation ---

    # Check if arr is actually a list
    if not isinstance(arr, list):
        raise TypeError(f"Expected input 'arr' to be a list, got {type(arr).__name__}")

    # Check if target is a numeric type
    if not isinstance(target, (int, float)):
        raise TypeError(f"Expected 'target' to be an int or float, got {type(target).__name__}")

    # Handle empty list edge case
    if len(arr) == 0:
        return False

    # Ensure all elements in the list are numeric
    for element in arr:
        if not isinstance(element, (int, float)):
            raise TypeError(f"All elements in 'arr' must be numeric. Found: {type(element).__name__}")

    # Verify that the list is sorted in non-decreasing order
    # This is a requirement for binary search to function correctly
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            raise ValueError("The input list 'arr' must be sorted in non-decreasing order.")

    # --- Binary Search Logic ---

    # Initialize the boundary pointers
    left_index: int = 0
    right_index: int = len(arr) - 1

    while left_index <= right_index:
        # Calculate the midpoint
        # Using floor division to ensure an integer index
        # (left + right) // 2 is safe in Python as it handles arbitrarily large integers
        mid_index: int = (left_index + right_index) // 2

        # Retrieve the value at the midpoint
        current_value: Union[int, float] = arr[mid_index]

        # Check if the midpoint value is the target
        if current_value == target:
            return True

        # If the current value is smaller than the target, 
        # the target must be in the right half.
        elif current_value < target:
            # Update the left boundary to be one position past the midpoint
            left_index = mid_index + 1

        # If the current value is larger than the target,
        # the target must be in the left half.
        else:
            # Update the right boundary to be one position before the midpoint
            right_index = mid_index - 1

    # If the loop finishes without returning, the target is not in the list
    return False

# Explicitly checking the provided assertions
if __name__ == "__main__":
    # The problem asks for the function to satisfy these specific assertions:
    assert binary_search([1, 2, 3, 5, 8], 6) == False
    assert binary_search([7, 8, 9, 10, 13], 10) == True
    assert binary_search([11, 13, 14, 19, 22, 36], 23) == False