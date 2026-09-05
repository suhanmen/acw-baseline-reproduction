def max_sum_increasing_subseq(nums: list[int], n: int, k: int, idx: int) -> int:
    """
    Find the maximum sum of an increasing subsequence that:
      - Lies entirely within nums[0:i+1] (prefix till ith index, inclusive)
      - AND includes the element at index 'k' (where k > i)

    Parameters:
      nums: list of integers
      n: length of nums (unused for logic but kept for signature consistency if needed)
      k: index of the required element to include (must be > i)
      idx: the 'ith' index defining the prefix limit (0-based)

    Returns:
      Maximum sum satisfying the conditions, or 0 if no such subsequence exists.
    """
    if idx < 0 or k >= len(nums) or k <= idx:
        return 0

    # Ensure we only consider up to index idx for the increasing part
    limit = idx

    # dp[i] = maximum sum of increasing subsequence ending at index i (where i <= limit)
    dp = [0] * (limit + 1)

    # Base case: each element alone
    for i in range(limit + 1):
        dp[i] = nums[i]

    # Build DP table
    for i in range(1, limit + 1):
        for j in range(i):
            if nums[j] < nums[i]:
                if dp[j] + nums[i] > dp[i]:
                    dp[i] = dp[j] + nums[i]

    best = 0
    for i in range(limit + 1):
        if nums[i] < nums[k]:
            if dp[i] + nums[k] > best:
                best = dp[i] + nums[k]

    return best if best > 0 else 0