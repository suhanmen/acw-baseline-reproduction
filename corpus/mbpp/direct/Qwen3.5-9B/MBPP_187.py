def longest_common_subsequence(s1: str, s2: str, m: int, n: int) -> int:
    """
    Returns the length of the longest common subsequence of s1[0:m] and s2[0:n].
    The function uses dynamic programming with O(m*n) time and O(m*n) space.
    """
    if m == 0 or n == 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]