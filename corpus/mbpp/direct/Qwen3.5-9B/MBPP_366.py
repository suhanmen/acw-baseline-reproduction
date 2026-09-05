def adjacent_num_product(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements")
    max_product = nums[0] * nums[1]
    for i in range(1, len(nums) - 1):
        product = nums[i] * nums[i + 1]
        if product > max_product:
            max_product = product
    return max_product