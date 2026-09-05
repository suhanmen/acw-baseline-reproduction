def is_subset_sum(nums, n, k):
    """
    Determines if there is a subset of 'nums' with exactly 'k' elements
    whose sum equals 'n'.

    Args:
        nums (List[int]): The list of integers.
        n (int): The required sum.
        k (int): The required number of elements in the subset.

    Returns:
        bool: True if such a subset exists, False otherwise.
    """
    if k == 0:
        return n == 0
    if k < 0 or len(nums) < k:
        return False

    # dp[i][j] will be True if a subset of first i numbers has exactly j elements
    # and sums to n. However, since n is fixed, we only need to track count of elements.
    # We need to track: count of elements AND current sum.
    # Let dp[count] be a set of achievable sums using exactly 'count' elements.

    dp = {0}  # count=0, sum=0
    for num in nums:
        # Iterate backwards to avoid using same element multiple times for same count step
        # But here we need to update all counts. Let's use a list of sets.
        # Actually, standard DP for "subset with size k and sum n":
        # dp[j][s] = boolean, can we get sum s with j elements?
        # Dimensions: (k+1) x (n+1)
        pass

    # Re-implementation with 2D DP
    # dp[i][j] = True if we can get sum j using i elements from processed numbers
    dp = [[False] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = True

    for num in nums:
        # Iterate backwards from k-1 down to 0 to update dp[i+1]
        for i in range(k - 1, -1, -1):
            for j in range(0, n - num + 1):
                if dp[i][j]:
                    dp[i+1][j + num] = True

    return dp[k][n]


# Verification against assertions
if __name__ == "__main__":
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 9) == True
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 30) == False
    assert is_subset_sum([3, 34, 4, 12, 5, 2], 6, 15) == True