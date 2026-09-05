def sum_three_smallest_nums(nums):
    return sum(sorted([n for n in nums if n > 0])[:3])