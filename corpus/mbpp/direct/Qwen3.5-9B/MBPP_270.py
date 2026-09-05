def sum_even_and_even_index(nums, n):
    total = 0
    for i in range(0, n, 2):
        if i + 1 < len(nums):
            index = i
            if nums[index] % 2 == 0:
                total += nums[index]
    return total