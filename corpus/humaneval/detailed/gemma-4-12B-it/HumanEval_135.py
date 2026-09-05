from typing import List, Any

def can_arrange(arr: List[Any]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    # --- Input Validation ---
    # Ensure the input is a list.
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")

    # According to the problem statement, the array will not contain duplicate values.
    # While we assume the input follows this, we treat any list with 0 or 1 elements
    # as having no "preceding" elements to compare against for the first index.

    # Handle empty list case
    if len(arr) == 0:
        return -1

    # Handle single element list case
    # There is no preceding element for index 0, so no element satisfies the condition.
    if len(arr) == 1:
        return -1

    # --- Logic Implementation ---
    # The goal is to find the LARGEST index i such that arr[i] < arr[i-1].
    # Since the problem states there are no duplicate values, 
    # "not greater than or equal to" is equivalent to "strictly less than".

    # We initialize our result to -1.
    last_found_index = -1

    # We start iterating from index 1 because index 0 has no predecessor.
    # We iterate forward to find all valid indices, keeping track of the largest.
    for current_index in range(1, len(arr)):
        current_value = arr[current_index]
        previous_value = arr[current_index - 1]

        # Check the condition: current element is not greater than or equal to predecessor.
        # In a set with no duplicates, this means current_value < previous_value.
        is_not_greater_or_equal = current_value < previous_value

        if is_not_greater_or_equal:
            # If condition is met, update the last_found_index.
            # Because we are iterating from left to right, the last one we find 
            # will naturally be the largest index.
            last_found_index = current_index

    return last_found_index

# Helper check for the logic:
# Example 1: [1, 2, 4, 3, 5]
# Index 1: 2 < 1? False
# Index 2: 4 < 2? False
# Index 3: 3 < 4? True -> last_found_index = 3
# Index 4: 5 < 3? False
# Result: 3. Correct.

# Example 2: [1, 2, 3]
# Index 1: 2 < 1? False
# Index 2: 3 < 2? False
# Result: -1. Correct.