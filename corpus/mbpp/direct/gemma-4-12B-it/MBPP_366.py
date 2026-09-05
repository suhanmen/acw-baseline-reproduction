def adjacent_num_product(nums):
    """
    Finds the largest product of the pair of adjacent elements from a given list of integers.
    """
    if len(nums) < 2:
        return 0

    max_product = float('-inf')
    for i in range(len(nums) - 1):
        product = nums[i] * nums[i+1]
        if product > max_product:
            max_product = product

    return max_product