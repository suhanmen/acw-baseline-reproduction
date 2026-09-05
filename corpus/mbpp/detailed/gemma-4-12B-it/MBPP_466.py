from typing import List

def find_peak_element(nums: List[int], size: int) -> int:
    """
    Finds the index of a peak element in an array.
    A peak element is an element that is strictly greater than its neighbors.
    For elements at the boundaries, the neighbor that doesn't exist is 
    considered to be negative infinity.

    The function uses a binary search approach to achieve O(log n) complexity.

    Args:
        nums: A list of integers.
        size: The length of the list.

    Returns:
        int: The index of a peak element.

    Raises:
        ValueError: If the input list is empty or size is invalid.
        TypeError: If the input types are incorrect.
    """
    # --- Input Validation ---
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list of integers.")

    if not isinstance(size, int):
        raise TypeError("Input 'size' must be an integer.")

    if size <= 0:
        # Handling the degenerate case of an empty or invalid size
        # Based on the assertions, size is usually 1 or more.
        raise ValueError("Array size must be greater than zero.")

    if len(nums) != size:
        raise ValueError(f"Provided size {size} does not match list length {len(nums)}.")

    # --- Edge Case Handling ---
    # Single element array: the only element is the peak
    if size == 1:
        return 0

    # --- Binary Search Logic ---
    # We aim to find a local maximum. If an element is smaller than its 
    # neighbor to the right, a peak must exist on the right side.
    # Otherwise, a peak must exist on the left side (including the current index).

    left_index = 0
    right_index = size - 1

    while left_index < right_index:
        # Calculate midpoint using floor division
        mid_index = left_index + (right_index - left_index) // 2

        # Compare the middle element with its immediate right neighbor
        current_value = nums[mid_index]
        next_value = nums[mid_index + 1]

        if current_value < next_value:
            # We are on an upward slope. 
            # The peak must be to the right of mid_index.
            left_index = mid_index + 1
        else:
            # We are on a downward slope or at a local peak.
            # The peak is either mid_index or to the left of mid_index.
            right_index = mid_index

    # After the loop, left_index == right_index, pointing to a peak.
    return left_index

def find_peak(nums: List[int], size: int) -> int:
    """
    Wrapper function to match the required signature exactly.
    """
    # Perform validation and calculation
    # The problem asks for the index of the peak element.
    peak_index = find_peak_element(nums, size)
    return peak_index

# The following assertions are provided in the problem description to verify correctness.
if __name__ == "__main__":
    # These are used for internal verification of the logic.
    assert find_peak([1, 3, 20, 4, 1, 0], 6) == 2
    assert find_peak([2, 3, 4, 5, 6], 5) == 4
    assert find_peak([8, 9, 11, 12, 14, 15], 6) == 5