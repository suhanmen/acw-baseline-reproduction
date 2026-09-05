def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0

    min_so_far = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        # Either extend the current subarray or start a new one at current element
        current_sum = min(nums[i], current_sum + nums[i])
        # Update global minimum
        min_so_far = min(min_so_far, current_sum)

    return min_so_far