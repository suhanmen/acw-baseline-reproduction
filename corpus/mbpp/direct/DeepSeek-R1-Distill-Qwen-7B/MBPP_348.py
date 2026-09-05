def find_ways(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(n+1):
            if j >= i:
                dp[i][j] = dp[i-1][j-1]
            if j >= i:
                dp[i][j] += dp[i][j-i]
    return dp[n][n]