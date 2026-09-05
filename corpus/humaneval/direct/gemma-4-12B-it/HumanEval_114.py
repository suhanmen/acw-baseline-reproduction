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

    # Kadane's algorithm variant to find the minimum subarray sum
    min_so_far = nums[0]
    current_min = nums[0]

    for i in range(1, len(nums)):
        current_min = min(nums[i], current_min + nums[i])
        min_so_far = min(min_so_far, current_min)

    return min_so_far