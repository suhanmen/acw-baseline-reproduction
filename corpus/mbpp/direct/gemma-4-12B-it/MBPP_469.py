def max_profit(prices: list[int], k: int) -> int:
    """
    Finds the maximum profit from at most k stock transactions.

    Args:
        prices: A list of stock prices over time.
        k: The maximum number of transactions allowed.

    Returns:
        The maximum profit possible.
    """
    if not prices or k == 0:
        return 0

    # Optimization: If k is larger than half the number of days, 
    # it's equivalent to the unlimited transactions problem.
    if k >= len(prices) // 2:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    # dp[i][j] represents the max profit using at most i transactions
    # up to day j.
    # To save space, we can use a 1D array or just manage the current/prev row.
    # dp[i][j] = max(dp[i][j-1], prices[j] + max(dp[i-1][m] - prices[m] for m < j))

    dp = [[0] * len(prices) for _ in range(k + 1)]

    for i in range(1, k + 1):
        # max_diff tracks the maximum of (dp[i-1][m] - prices[m])
        max_diff = -prices[0]
        for j in range(1, len(prices)):
            dp[i][j] = max(dp[i][j-1], prices[j] + max_diff)
            max_diff = max(max_diff, dp[i-1][j] - prices[j])

    return dp[k][len(prices) - 1]

if __name__ == "__main__":
    assert max_profit([1, 5, 2, 3, 7, 6, 4, 5], 3) == 10
    assert max_profit([2, 4, 7, 5, 4, 3, 5], 2) == 7
    assert max_profit([10, 6, 8, 4, 2], 2) == 2