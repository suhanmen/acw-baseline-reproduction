def find_longest_repeating_subseq(s: str) -> int:
    n = len(s)
    # dp[i][j] = length of longest repeating subsequence with different chars at same positions
    # considering prefixes s[:i+1] and s[:j+1], and we only allow s[i] != s[j]
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if s[i] != s[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

    return dp[0][1] if n > 1 else 0