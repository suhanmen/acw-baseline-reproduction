def check_Consecutive(nums):
    if not nums:
        return False
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i + 1] - sorted_nums[i] != 1:
            return False
    return True