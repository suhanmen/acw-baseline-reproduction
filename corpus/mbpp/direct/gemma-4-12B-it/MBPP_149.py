def longest_subseq_with_diff_one(arr, n):
    if not arr:
        return 0

    # dp[x] stores the length of the longest valid subsequence ending with value x
    dp = {}
    max_len = 0

    for num in arr:
        # A subsequence ending in num can be formed by appending num 
        # to a subsequence ending in num-1 or num+1.
        # We take the maximum length from either neighbor and add 1.
        prev_minus = dp.get(num - 1, 0)
        prev_plus = dp.get(num + 1, 0)

        dp[num] = max(prev_minus, prev_plus) + 1

        if dp[num] > max_len:
            max_len = dp[num]

    return max_len