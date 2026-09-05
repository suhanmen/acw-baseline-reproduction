from typing import List

def find_missing(nums: List[int], n: int) -> int:
    """
    Finds the missing number in a sorted list of integers.

    The function assumes the list contains distinct integers in increasing order,
    representing a sequence of numbers from 1 to n, where exactly one 
    number is missing.

    Args:
        nums: A sorted list of integers.
        n: The maximum value expected in the sequence (1 to n).

    Returns:
        The missing integer.

    Raises:
        ValueError: If input list is empty, contains duplicates, 
                    is not sorted, or if the count of elements is incorrect.
    """
    # --- Input Validation ---

    # Check if the input is a list
    if not isinstance(nums, list):
        raise ValueError("Input 'nums' must be a list.")

    # Check if the expected range n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The value of 'n' must be a positive integer.")

    # The list must have exactly n-1 elements if one is missing
    expected_length = n - 1
    actual_length = len(nums)

    if actual_length != expected_length:
        raise ValueError(
            f"List length {actual_length} does not match expected "
            f"length {expected_length} for a sequence of 1 to {n} missing one value."
        )

    # Handle the case where n=1 (list should be empty, but problem implies 1 to n)
    if n == 1:
        if actual_length == 0:
            return 1
        else:
            raise ValueError("List should be empty for n=1.")

    # Check for sorted order and duplicates
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            raise ValueError("The input list must be sorted in strictly increasing order.")

    # --- Logic ---

    # Strategy: Binary Search
    # In a perfect sequence 1, 2, 3... i, the value at index i should be i + 1.
    # If nums[i] > i + 1, it means the missing number is to the left (or is the current index).

    low_index = 0
    high_index = len(nums) - 1
    missing_number = -1

    # Handle edge cases for boundaries first
    # Case 1: The missing number is at the very beginning (1)
    if nums[0] != 1:
        return 1

    # Case 2: The missing number is at the very end (n)
    if nums[-1] != n:
        return n

    # Binary Search for the "gap"
    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2

        # The value at mid_index should ideally be (mid_index + 1)
        # If it is, the missing number is in the right half.
        expected_value = mid_index + 1
        actual_value = nums[mid_index]

        if actual_value == expected_value:
            # Everything is correct up to this point, look right
            low_index = mid_index + 1
        else:
            # The value is larger than expected, so the gap is to the left
            # This index is a candidate for the "point of divergence"
            missing_number = expected_value
            high_index = mid_index - 1

    # If binary search finishes and no specific gap was caught, 
    # it's a logical impossibility given the initial checks,
    # but we return missing_number or n as a fallback.
    if missing_number == -1:
        return n

    return missing_number