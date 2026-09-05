def add_consecutive_nums(nums):
    if not nums:
        return []
    result = []
    i = 0
    while i < len(nums) - 1:
        if nums[i] + 1 == nums[i + 1]:
            result.append(nums[i] + nums[i + 1])
            i += 2
        else:
            i += 1
    return result