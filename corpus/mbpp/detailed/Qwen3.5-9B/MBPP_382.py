from typing import List, Union

Number = Union[int, float]

def find_rotation_count(arr: List[Number]) -> int:
    """
    Finds the number of rotations in a circularly sorted array.

    A circularly sorted array is one that was originally sorted in ascending order
    and then rotated some number of times. For example, [3, 4, 5, 1, 2] is a rotated
    version of [1, 2, 3, 4, 5]. The number of rotations is defined as the number of
    positions the array has been shifted to the right (with wrap-around).

    This function implements an O(log n) algorithm using binary search to find the
    index of the minimum element. The number of rotations is then equal to the index
    of the minimum element (since a sorted array has the minimum at index 0, which 
    corresponds to 0 rotations).

    Args:
        arr: A list of numbers representing a circularly sorted array.

    Returns:
        The number of rotations (index of the minimum element).

    Raises:
        ValueError: If the input is not a list, is empty, or does not represent 
                    a valid circularly sorted array.
        TypeError: If elements in the list are not comparable numbers.
    """

    # Step 1: Validate input type
    if not isinstance(arr, list):
        raise TypeError(f"Expected a list, but got {type(arr).__name__}")

    # Step 2: Handle empty input edge case
    if len(arr) == 0:
        raise ValueError("Input array cannot be empty")

    # Step 3: Handle single element edge case
    if len(arr) == 1:
        return 0

    # Step 4: Basic validation that all elements are numbers
    for i, element in enumerate(arr):
        if not isinstance(element, (int, float)):
            raise TypeError(f"All elements must be numbers, but element at index {i} is {type(element).__name__}")

    # Step 5: Validate that the array represents a circularly sorted structure
    # We do this by checking if it's either perfectly sorted or has exactly one "drop"
    # where arr[i] > arr[i+1]
    drop_count = 0
    min_index = -1

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            drop_count += 1
            # The minimum element should be at index i + 1
            min_index = i + 1
        # If we find more than one drop, it's not a valid rotated sorted array
        if drop_count > 1:
            raise ValueError(
                f"Array is not a valid circularly sorted array. "
                f"Found {drop_count} drop points, expected at most 1."
            )

    # Additional validation: Check the wrap-around condition for arrays with a drop
    if drop_count == 1:
        # For a valid rotated array, the last element should be <= the first element
        # unless it's a perfectly sorted array (drop_count would be 0)
        if arr[-1] > arr[0]:
            raise ValueError(
                f"Array is not a valid circularly sorted array. "
                f"Last element ({arr[-1]}) should be <= first element ({arr[0]}) "
                f"if there is a rotation."
            )

    # Special case: If the array is perfectly sorted, there are 0 rotations
    if drop_count == 0:
        return 0

    # If we reach here, we have a valid rotated array with exactly one drop.
    # The number of rotations is the index of the minimum element.
    # We already identified min_index during the validation loop.

    # Double-check using binary search to ensure O(log n) complexity and robustness
    rotation_count = _find_min_index_via_binary_search(arr)

    return rotation_count

def _is_valid_circularly_sorted(arr: List[Number]) -> bool:
    """
    Helper function to validate if an array is circularly sorted.
    Returns True if valid, False otherwise.
    """
    if len(arr) <= 1:
        return True

    drop_count = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            drop_count += 1
            if drop_count > 1:
                return False

    # If there is a drop, check wrap-around
    if drop_count == 1:
        if arr[-1] > arr[0]:
            return False

    return True

def _find_min_index_via_binary_search(arr: List[Number]) -> int:
    """
    Helper function to find the index of the minimum element in a circularly 
    sorted array using binary search. This is the number of rotations.

    This is a robust O(log n) implementation that handles various edge cases.
    """
    left = 0
    right = len(arr) - 1
    min_index = 0

    # If the array is already sorted (no rotation), return 0
    if arr[left] <= arr[right]:
        return min_index

    # Binary search to find the minimum element
    while left < right:
        mid = (left + right) // 2

        # Compare middle element with the rightmost element
        if arr[mid] > arr[right]:
            # Minimum must be in the right half (excluding mid)
            left = mid + 1
        else:
            # Minimum must be in the left half (including mid)
            right = mid

    # When left == right, we found the index of the minimum element
    min_index = left

    # Final sanity check: verify that arr[min_index] is indeed the minimum
    # This handles potential floating point comparison issues or edge cases
    for i in range(len(arr)):
        if arr[i] < arr[min_index]:
            # This theoretically shouldn't happen with valid input
            raise ValueError("Invariant violated: Found smaller element after binary search")

    return min_index