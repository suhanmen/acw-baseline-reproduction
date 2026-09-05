def max_product(nums, n):
    """
    Find the maximum product formed by multiplying numbers of an increasing subsequence of that array.

    Args:
        nums (List[int]): List of integers.
        n (int): Length of the list (should match len(nums)).

    Returns:
        int: Maximum product of an increasing subsequence.
    """
    if n == 0 or len(nums) != n:
        return 0

    # dp[i] will store the maximum product of an increasing subsequence ending at index i
    dp = [1] * n

    # Max product seen so far
    max_prod = nums[0]

    for i in range(1, n):
        current_max = nums[i]
        # Check all previous elements to extend an increasing subsequence
        for j in range(i):
            if nums[j] < nums[i]:
                current_max = max(current_max, dp[j] * nums[i])
        dp[i] = current_max
        max_prod = max(max_prod, current_max)

    return max_prod