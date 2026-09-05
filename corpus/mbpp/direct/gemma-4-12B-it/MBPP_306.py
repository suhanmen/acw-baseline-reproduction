def max_sum_increasing_subseq(arr, n, i, k):
    """
    Finds the maximum sum of an increasing subsequence that:
    1. Ends at some index j where 0 <= j <= i.
    2. Includes the element at index k (where k > i).
    3. The subsequence remains strictly increasing.

    To satisfy the "including kth element" while being an increasing subsequence,
    the subsequence must consist of elements from the prefix [0...i] that are 
    smaller than arr[k], plus arr[k] itself.
    """
    # msis[j] will store the maximum sum of an increasing subsequence 
    # ending exactly at index j.
    msis = [0] * n

    # Standard Maximum Sum Increasing Subsequence (MSIS) algorithm
    # but we only care about elements in the prefix up to index i
    # that are also smaller than arr[k].
    for j in range(n):
        msis[j] = arr[j]
        for prev in range(j):
            if arr[prev] < arr[j]:
                msis[j] = max(msis[j], msis[prev] + arr[j])

    # The problem asks for the max sum of an increasing subsequence from 
    # the prefix [0...i] that can be extended by arr[k].
    # For arr[k] to extend a subsequence ending at index j, 
    # we must have j <= i AND arr[j] < arr[k].

    max_sum = 0
    # Check all possible ending positions j in the prefix [0...i]
    for j in range(i + 1):
        if arr[j] < arr[k]:
            # If valid, the sum is the MSIS ending at j + the value at k
            # However, we need to ensure the MSIS ending at j only used
            # elements smaller than arr[k]. 
            # Let's refine the approach:
            pass

    # Re-calculating MSIS specifically for elements < arr[k] within the prefix i
    # to ensure the subsequence ending at j is strictly increasing and can include arr[k]
    dp = [0] * (i + 1)
    for j in range(i + 1):
        if arr[j] < arr[k]:
            dp[j] = arr[j]
            for prev in range(j):
                if arr[prev] < arr[j] and arr[prev] < arr[k]:
                    dp[j] = max(dp[j], dp[prev] + arr[j])

    # The max sum is the max of dp[j] + arr[k] for all j in 0..i
    # If no such j exists (i.e., all prefix elements >= arr[k]), 
    # the subsequence is just [arr[k]]
    res = arr[k]
    for j in range(i + 1):
        if arr[j] < arr[k]:
            res = max(res, dp[j] + arr[k])

    return res

# Re-evaluating the logic based on the assertions:
# assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11
# Prefix [0..4] is [1, 101, 2, 3, 100], arr[6] is 5.
# Increasing subsequences in prefix ending with value < 5: 
# [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3].
# Max sum ending with value < 5 is (1+2+3) = 6.
# Total sum = 6 + arr[6] = 6 + 5 = 11. Matches.

# assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 2, 5) == 7
# Prefix [0..2] is [1, 101, 2], arr[5] is 4.
# Values < 4 in prefix are [1, 2].
# Max sum of increasing subseq ending with value < 4 is (1+2) = 3.
# Total sum = 3 + arr[5] = 3 + 4 = 7. Matches.

# assert max_sum_increasing_subseq([11, 15, 19, 21, 26, 28, 31], 7, 2, 4) == 71
# Prefix [0..2] is [11, 15, 19], arr[4] is 26.
# All values in prefix [11, 15, 19] are < 26.
# Max sum of increasing subseq in prefix is (11+15+19) = 45.
# Total sum = 45 + arr[4] = 45 + 26 = 71. Matches.

# The logic is: 
# 1. Consider only elements in arr[0...i] that are strictly less than arr[k].
# 2. Find the maximum sum of an increasing subsequence using these elements.
# 3. Add arr[k] to that sum.

def max_sum_increasing_subseq(arr, n, i, k):
    target_val = arr[k]
    # dp[j] is the max sum of an increasing subsequence ending at index j
    # where all elements in the subsequence are < target_val and j <= i.
    dp = [0] * n
    max_prefix_sum = 0

    for j in range(i + 1):
        if arr[j] < target_val:
            dp[j] = arr[j]
            for prev in range(j):
                if arr[prev] < arr[j] and arr[prev] < target_val:
                    dp[j] = max(dp[j], dp[prev] + arr[j])
            max_prefix_sum = max(max_prefix_sum, dp[j])

    return max_prefix_sum + target_val