def diff_consecutivenums(nums):
    result = [b-a for a, b in zip(nums[:-1], nums[1:])]
    return result