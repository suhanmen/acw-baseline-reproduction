def multiply_num(nums):
    result = 1.0
    for num in nums:
        result *= num
    return result / len(nums)