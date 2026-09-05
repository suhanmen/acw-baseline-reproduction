def no_of_subsequences(nums, k):
    if k <= 1:
        return 0
    n = len(nums)
    count = 0
    # Generate all non-empty subsequences
    for i in range(1, 1 << n):
        product = 1
        valid = True
        for j in range(n):
            if i & (1 << j):
                product *= nums[j]
                if product >= k:
                    valid = False
                    break
        if valid:
            count += 1
    return count