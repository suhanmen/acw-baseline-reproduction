def find_longest_repeating_subseq(s: str) -> int:
    """
    Finds the length of the longest repeating subsequence of a string.
    A subsequence is repeating if the characters at the same positions
    in the original string are not used for the same character in the subsequence.

    This is solved using Dynamic Programming by finding the Longest Common 
    Subsequence (LCS) of the string with itself, with the added 
    constraint that the indices of the characters must be different.
    """
    n = len(s)
    # Create a 2D DP table initialized to 0
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If characters match AND indices are different
            if s[i-1] == s[j-1] and i != j:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # Otherwise, take the maximum from the top or left cell
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][n]