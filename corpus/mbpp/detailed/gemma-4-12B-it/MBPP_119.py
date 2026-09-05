from typing import List

def search(nums: List[int], length: int) -> int:
    """
    Finds the element that appears only once in a sorted array.

    Args:
        nums: A sorted list of integers where every element except one
              appears exactly twice.
        length: The total number of elements in the array.

    Returns:
        The single integer that appears only once in the array.

    Raises:
        ValueError: If input validation fails.
        IndexError: If the array is empty or length is invalid.
    """
    # Input Validation
    if not isinstance(nums, list):
        raise ValueError("Input 'nums' must be a list.")

    if not isinstance(length, int):
        raise ValueError("Input 'length' must be an integer.")

    actual_length = len(nums)

    if actual_length == 0:
        raise IndexError("The input array is empty.")

    if actual_length != length:
        raise ValueError(f"Provided length {length} does not match actual list size {actual_length}.")

    # Edge Case: Only one element in the array
    if actual_length == 1:
        return nums[0]

    # Binary search approach to find the single element in O(log n) time.
    # In a sorted array where every element appears twice except one,
    # the single element's position determines the "pairing" of previous elements.

    low = 0
    high = actual_length - 1

    while low <= high:
        # If the search space has one element
        if low == high:
            return nums[low]

        mid = (low + high) // 2

        # Ensure mid is even for easier pairing logic.
        # If mid is odd, decrement it to make it even.
        # This ensures that nums[mid] and nums[mid+1] are a potential pair.
        if mid % 2 != 0:
            mid -= 1

        # Check if the pair at mid and mid+1 is consistent.
        # If the element at mid is the same as the element at mid+1,
        # it means the single element must be located to the right of mid+1.
        if nums[mid] == nums[mid + 1]:
            # The single element is in the right half
            low = mid + 2
        else:
            # The single element is in the left half (including mid)
            high = mid

    # This part should ideally not be reached given the problem constraints,
    # but we return low as a fallback.
    return nums[low]

# The problem asks for the function to satisfy specific assertions.
# The logic above uses binary search to find the unique element in O(log n).