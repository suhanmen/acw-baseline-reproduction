from typing import List

def find_Min(nums: List[int], start: int, end: int) -> int:
    """
    Finds the minimum element in a sorted and rotated array using binary search.

    Args:
        nums: A list of integers sorted in ascending order and then rotated.
        start: The starting index of the range to search.
        end: The ending index of the range to search.

    Returns:
        The minimum integer found in the specified range.

    Raises:
        ValueError: If the input list is empty or indices are out of bounds.
        TypeError: If inputs are of incorrect types.
    """
    # --- Input Validation ---
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list of integers.")

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Indices 'start' and 'end' must be integers.")

    if not nums:
        raise ValueError("The input list 'nums' cannot be empty.")

    if start < 0 or end >= len(nums) or start > end:
        raise ValueError(
            f"Indices are out of bounds. List length: {len(nums)}, "
            f"start: {start}, end: {end}"
        )

    # --- Binary Search Logic ---
    # The goal is to find the 'pivot' point where the rotation occurred.
    # In a sorted and rotated array, the minimum element is the only 
    # element whose predecessor is greater than it.

    left_ptr = start
    right_ptr = end

    # If the range is already sorted (not rotated or rotated back to original),
    # the first element is the minimum.
    if nums[left_ptr] <= nums[right_ptr]:
        return nums[left_ptr]

    while left_ptr <= right_ptr:
        # Calculate midpoint safely to avoid potential overflow in other languages
        # though Python handles large integers automatically.
        mid_idx = (left_ptr + right_ptr) // 2
        mid_val = nums[mid_idx]

        # Check if mid_idx is the minimum element
        # Case 1: The element at mid_idx is smaller than its predecessor
        if mid_idx > start and nums[mid_idx] < nums[mid_idx - 1]:
            return nums[mid_idx]

        # Case 2: The element at mid_idx-1 is the minimum element
        # (meaning mid_idx is the first element of the second sorted half)
        if mid_idx > start and nums[mid_idx - 1] < nums[mid_idx] and \
           nums[mid_idx - 1] < nums[mid_idx - 2]:
            # This check is slightly redundant but keeps logic explicit
            pass

        # Determine which half to search next.
        # If the middle element is greater than the leftmost element,
        # the pivot (minimum) must be in the right half.
        if nums[mid_idx] >= nums[left_ptr]:
            left_ptr = mid_idx + 1
        else:
            # If the middle element is smaller than the leftmost element,
            # the pivot (minimum) is in the left half (including mid_idx).
            right_ptr = mid_idx - 1

    # Fallback: If the loop terminates without an explicit return,
    # it means the smallest element is at the current left_ptr.
    # This handles cases where the array is very small.
    if left_ptr <= end:
        return nums[left_ptr]

    # This part should theoretically not be reached given valid inputs.
    return nums[start]