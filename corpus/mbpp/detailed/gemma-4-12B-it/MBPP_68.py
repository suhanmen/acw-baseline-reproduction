from typing import List

def is_Monotonic(nums: List[int]) -> bool:
    """
    Determines whether a given list of integers is monotonic.
    A sequence is monotonic if it is either entirely non-increasing 
    or entirely non-decreasing.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        bool: True if the list is monotonic, False otherwise.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
        ValueError: If the input list is None.
    """
    # Validate input type
    if nums is None:
        raise ValueError("Input list cannot be None.")

    if not isinstance(nums, list):
        raise TypeError(f"Input must be a list, received {type(nums).__name__}")

    # Check for non-integer elements
    for item in nums:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers, found {type(item).__name__}")

    # Handle edge cases: empty list or single element list
    # By definition, an empty list or a list with one element is monotonic.
    list_length = len(nums)
    if list_length <= 1:
        return True

    # Track state variables for monotonicity
    # We assume the list could be both non-increasing and non-decreasing 
    # until we find evidence to the contrary.
    is_non_increasing = True
    is_non_decreasing = True

    # Iterate through the list to check the relationship between adjacent elements
    for i in range(list_length - 1):
        current_element = nums[i]
        next_element = nums[i + 1]

        # Check if it violates the non-increasing property
        # (i.e., if the next element is strictly greater than the current)
        if next_element > current_element:
            is_non_increasing = False

        # Check if it violates the non-decreasing property
        # (i.e., if the next element is strictly smaller than the current)
        if next_element < current_element:
            is_non_decreasing = False

        # Optimization: if both flags are False, it cannot be monotonic
        if not is_non_increasing and not is_non_decreasing:
            return False

    # The list is monotonic if it satisfies at least one of the conditions
    final_result = is_non_increasing or is_non_decreasing
    return final_result