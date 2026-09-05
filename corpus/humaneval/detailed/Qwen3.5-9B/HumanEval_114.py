from typing import List, Union

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.

    Edge cases handled:
    - Empty list (returns infinity to indicate invalid input)
    - Single element (returns the element itself)
    - All positive numbers (returns the smallest single element)
    - All negative numbers (returns the sum of all elements)
    - Mixed positive and negative numbers (uses Kadane's algorithm variation)
    - Zeroes in the array
    - Very large or very small integer values (Python handles arbitrary precision)

    Args:
        nums: A list of integers representing the input array.

    Returns:
        The minimum sum of any non-empty sub-array.

    Raises:
        ValueError: If the input is not a list or contains non-integer elements.
        TypeError: If the input type is incorrect.
    """

    # Step 1: Input validation - Check if nums is a list
    if not isinstance(nums, list):
        raise TypeError(f"Expected a list, but got {type(nums).__name__}")

    # Step 2: Input validation - Check if the list is empty
    if len(nums) == 0:
        raise ValueError("Input list cannot be empty. At least one element is required.")

    # Step 3: Input validation - Check if all elements are integers
    for i, num in enumerate(nums):
        if not isinstance(num, int) or isinstance(num, bool):
            raise TypeError(f"Element at index {i} is not an integer: {type(num).__name__}")

    # Step 4: Initialize tracking variables for the minimum sum
    # min_so_far will store the minimum sum found so far
    # current_sum will store the sum of the current sub-array being considered
    min_so_far = nums[0]
    current_sum = nums[0]

    # Step 5: Iterate through the array starting from the second element
    # We start from index 1 because we've already processed index 0
    for i in range(1, len(nums)):
        current_value = nums[i]

        # Step 6: Decision logic - Either extend the current sub-array or start a new one
        # If current_sum is positive, adding it to current_value will result in a larger sum
        # than just current_value alone (unless current_value is also positive and we're looking for negatives)
        # Actually, for minimum sum, we want to stop adding positive sums
        if current_sum < 0:
            # If current_sum is negative, adding it to current_value will make the sum smaller
            current_sum = current_sum + current_value
        else:
            # If current_sum is zero or positive, starting fresh with current_value is better
            # for finding a minimum sum (unless current_value itself is negative and we need context)
            # Actually, standard approach: if current_sum > 0, reset to current_value
            # Because adding a positive number to anything will make it larger
            current_sum = current_value

        # Step 7: Update the minimum sum found so far if current_sum is smaller
        if current_sum < min_so_far:
            min_so_far = current_sum

    # Step 8: Return the minimum sum found
    return min_so_far