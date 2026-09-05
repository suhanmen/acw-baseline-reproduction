def longest_common_subsequence(X: str, Y: str, m: int, n: int) -> int:
    """
    Finds the length of the longest common subsequence of two strings X and Y.

    Args:
        X: The first string.
        Y: The second string.
        m: Length of string X.
        n: Length of string Y.

    Returns:
        The length of the longest common subsequence.
    """
    # Create a 2D array to store lengths of LCS of substrings
    # dp[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table in bottom-up fashion
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]