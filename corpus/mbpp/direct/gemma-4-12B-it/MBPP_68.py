def is_Monotonic(nums):
    """
    Checks whether the given array is monotonic.
    An array is monotonic if it is either entirely non-increasing or entirely non-decreasing.
    """
    is_increasing = True
    is_decreasing = True

    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            is_decreasing = False
        if nums[i] > nums[i + 1]:
            is_increasing = False

    return is_increasing or is_decreasing