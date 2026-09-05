from typing import List


def max_subarray_product(nums: List[int]) -> int:
    """
    Finds the maximum product of a contiguous subarray within a given list of integers.

    This implementation uses a dynamic programming approach that tracks both the 
    maximum and minimum products ending at the current position. This is necessary 
    because a very small negative number multiplied by another negative number 
    can result in a large positive number.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The maximum product found.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list of integers.
    """
    # --- Input Validation ---
    if not isinstance(nums, list):
        raise TypeError("Input must be a list of integers.")

    if len(nums) == 0:
        raise ValueError("Input list cannot be empty.")

    for item in nums:
        if not isinstance(item, int):
            raise TypeError(f"All elements in the list must be integers. Found: {type(item)}")

    # --- Initialization ---
    # Handle the single element case explicitly
    if len(nums) == 1:
        return nums[0]

    # 'global_max' stores the highest product found across all subarrays seen so far.
    # 'current_max' stores the maximum product of a subarray ending at the current index.
    # 'current_min' stores the minimum product of a subarray ending at the current index.
    # (We need current_min because a negative * negative = positive).

    global_max = nums[0]
    current_max = nums[0]
    current_min = nums[0]

    # Iterate through the list starting from the second element
    for i in range(1, len(nums)):
        current_val = nums[i]

        # If the current value is negative, swapping current_max and current_min 
        # simplifies the logic because multiplying by a negative flips the signs.
        if current_val < 0:
            current_max, current_min = current_min, current_max

        # Calculate potential products. 
        # A subarray can either:
        # 1. Start at the current element (current_val)
        # 2. Continue the previous maximum product (current_max * current_val)

        # We use the swapped values if current_val was negative.
        option_a = current_val
        option_b = current_max * current_val

        # Update current_max for the current position
        current_max = max(option_a, option_b)

        # Update current_min for the current position
        # (Again, current_min was swapped earlier if current_val < 0)
        option_c = current_val
        option_d = current_min * current_val
        current_min = min(option_c, option_d)

        # Update the global maximum found so far
        if current_max > global_max:
            global_max = current_max

    return global_max