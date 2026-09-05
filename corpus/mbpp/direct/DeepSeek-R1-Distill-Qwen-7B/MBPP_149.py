def longest_subseq_with_diff_one(arr):
    from collections import defaultdict

    # Initialize a dictionary to keep track of the longest subsequence ending at each number
    dp = defaultdict(int)
    max_length = 0

    for num in arr:
        dp[num] = 1  # Each number itself is a subsequence of length 1

        # Check if num - 1 or num + 1 exists in the dictionary
        if (num - 1) in dp:
            dp[num] = max(dp[num], dp[num - 1] + 1)
        if (num + 1) in dp:
            dp[num] = max(dp[num], dp[num + 1] + 1)

        # Update the maximum length found so far
        if dp[num] > max_length:
            max_length = dp[num]

    return max_length

# Test cases
assert longest_subseq_with_diff_one([1, 2, 3, 4, 5, 3, 2], 7) == 6
assert longest_subseq_with_diff_one([10, 9, 4, 5, 4, 8, 6], 7) == 3
assert longest_subseq_with_diff_one([1, 2, 3, 2, 3, 7, 2, 1], 8) == 7