def adjacent_num_product(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two elements")
    if len(nums) == 2:
        return nums[0] * nums[1]

    max_product = nums[0] * nums[1]
    for i in range(1, len(nums)):
        current_product = nums[i] * nums[i + 1]
        if current_product > max_product:
            max_product = current_product
    return max_product