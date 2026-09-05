from typing import List

def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # Validate input types
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers.")

    # Check if all elements are integers
    for element in arr:
        if not isinstance(element, int):
            raise TypeError("All elements in the list must be integers.")

    # Handle edge cases: empty list or single element list are already palindromic
    n_elements = len(arr)
    if n_elements <= 1:
        return 0

    # We only need to compare elements from the start of the array 
    # with their corresponding elements at the end of the array.
    # We stop at the middle of the array.
    # For an even length (e.g., 4), we check indices (0, 3) and (1, 2).
    # For an odd length (e.g., 5), we check indices (0, 4) and (1, 3); 
    # the middle element (index 2) doesn't need a match.

    total_changes_needed = 0

    # Loop through the first half of the array
    # Using integer division ensures we handle both even and odd lengths correctly
    limit = n_elements // 2

    for i in range(limit):
        left_index = i
        right_index = n_elements - 1 - i

        left_value = arr[left_index]
        right_value = arr[right_index]

        # If the values at mirror positions are not equal, we must change one.
        # To minimize changes, we change one of these two to match the other.
        if left_value != right_value:
            total_changes_needed += 1

    return total_changes_needed