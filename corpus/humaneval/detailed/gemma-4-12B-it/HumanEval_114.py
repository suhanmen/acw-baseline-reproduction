from typing import List

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    # --- Input Validation ---

    # Check if input is a list
    if not isinstance(nums, list):
        raise TypeError(f"Input must be a list, but received {type(nums).__name__}")

    # Handle the empty list case
    # The problem asks for a non-empty sub-array. If the input itself is empty,
    # we cannot form a non-empty sub-array.
    if len(nums) == 0:
        raise ValueError("Input list 'nums' must contain at least one integer.")

    # Verify all elements are integers
    for i, element in enumerate(nums):
        if not isinstance(element, int):
            raise TypeError(f"Element at index {i} is {type(element).__name__}, expected int.")

    # --- Algorithm Logic ---

    # This is a variation of Kadane's Algorithm.
    # Standard Kadane's finds the maximum subarray sum.
    # To find the minimum subarray sum, we can either:
    # 1. Flip the logic of Kadane's (tracking current min instead of max).
    # 2. Negate all numbers, find max subarray sum, and negate the result.
    # We will implement option 1 for clarity.

    # Initialize the variable to track the minimum sum found so far.
    # We initialize it with the first element to handle the single-element case.
    current_min_sum = nums[0]
    global_min_sum = nums[0]

    # Iterate through the array starting from the second element (index 1)
    # because we used index 0 for initialization.
    for i in range(1, len(nums)):
        current_value = nums[i]

        # Logic: At each position, the minimum subarray ending here is 
        # either the current value itself OR the current value added to 
        # the minimum subarray ending at the previous position.

        # Option A: Start a new subarray at the current element.
        option_start_new = current_value

        # Option B: Extend the previous minimum subarray.
        option_extend_previous = current_min_sum + current_value

        # The minimum sum ending at index i is the lesser of these two.
        current_min_sum = min(option_start_new, option_extend_previous)

        # Update the global minimum if the local minimum is smaller.
        if current_min_sum < global_min_sum:
            global_min_sum = current_min_sum

    return global_min_sum