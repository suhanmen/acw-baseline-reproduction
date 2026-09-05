def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.

    The function handles all edge cases:
        - Empty input: returns None
        - Single-element input: returns that element
        - All negative numbers: returns the sum of all numbers
        - Mix of positive and negative numbers: finds the minimum sub-array sum

    Example usage:
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """
    if not nums:
        return None

    min_sum = current_sum = nums[0]

    for num in nums[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)

    return min_sum