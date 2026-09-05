def sum_three_smallest_nums(nums):
    positives = sorted(num for num in nums if num > 0)
    return sum(sorted_positives[:3])