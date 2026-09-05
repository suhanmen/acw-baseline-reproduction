def max_subarray_product(nums):
    if not nums:
        return 0

    # Initialize values with the first element
    max_so_far = nums[0]
    min_so_far = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]

        # When curr is negative, max_so_far and min_so_far swap roles
        # when multiplied by curr.
        if curr < 0:
            max_so_far, min_so_far = min_so_far, max_so_far

        # The max/min at the current position is either the current number
        # itself or the product of the current number and the previous max/min.
        max_so_far = max(curr, max_so_far * curr)
        min_so_far = min(curr, min_so_far * curr)

        # Update the overall maximum product found so far.
        result = max(result, max_so_far)

    return result