from typing import List

def find_rotation_count(nums: List[int]) -> int:
    """
    Finds the number of rotations in a circularly sorted array.
    A circularly sorted array is an array sorted in ascending order
    that has been rotated some number of positions.

    The number of rotations corresponds to the index of the minimum element.
    For example, [8, 9, 10, 1, 2] is rotated 3 times from [1, 2, 8, 9, 10].

    Args:
        nums (List[int]): A list of integers sorted in ascending order 
                           and then rotated.

    Returns:
        int: The number of rotations (index of the minimum element).

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list of integers.
    """
    # --- Input Validation ---
    if not isinstance(nums, list):
        raise TypeError("Input must be a list.")

    if not nums:
        # Depending on requirements, an empty list could be 0 or an error.
        # Given the nature of the problem, we treat it as an error or return 0.
        # Here, we raise a ValueError to ensure production-grade robustness.
        raise ValueError("Input list cannot be empty.")

    for item in nums:
        if not isinstance(item, int):
            raise TypeError("All elements in the list must be integers.")

    # --- Edge Case Handling ---
    # If the list has one element, it is rotated 0 times.
    if len(nums) == 1:
        return 0

    # If the first element is less than the last element, the array 
    # is already sorted and has 0 rotations.
    if nums[0] < nums[-1]:
        return 0

    # --- Core Logic ---
    # We use binary search to find the index of the minimum element.
    # The index of the minimum element is the rotation count.
    low = 0
    high = len(nums) - 1

    # We use a standard binary search approach to find the "pivot" point.
    while low <= high:
        # If the range has narrowed down to one element
        if low == high:
            return low

        mid = (low + high) // 2

        # Check if mid+1 is the minimum element.
        # This happens if nums[mid] is greater than nums[mid+1].
        # Example: [8, 9, 10, 1, 2] -> mid is 10, mid+1 is 1.
        if mid + 1 <= high and nums[mid] > nums[mid + 1]:
            return mid + 1

        # Check if mid itself is the minimum element.
        # This happens if nums[mid] is less than nums[mid-1].
        # Example: [8, 9, 10, 1, 2] -> mid is 1, mid-1 is 10.
        if mid - 1 >= low and nums[mid] < nums[mid - 1]:
            return mid

        # Decide which half to search.
        # If nums[mid] is greater than the first element, 
        # the pivot (minimum) must be in the right half.
        if nums[mid] >= nums[low]:
            low = mid + 1
        else:
            # Otherwise, the pivot is in the left half.
            high = mid - 1

    # Fallback for safety, though logic above covers all rotation cases.
    return 0