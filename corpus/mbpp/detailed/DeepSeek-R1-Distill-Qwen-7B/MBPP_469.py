python
def max_profit stock_transactions, k:
    """
    Find the maximum profit from a maximum of k stock transactions.

    This function calculates the maximum profit you can achieve by buying and selling
    stocks at most k times. The solution uses a dynamic programming approach to
    track the maximum profit after each possible number of transactions up to k.

    Args:
        stock_transactions (list): A list of integers representing the stock prices.
        k (int): The maximum number of transactions allowed.

    Returns:
        int: The maximum profit achievable with at most k transactions.

    Raises:
        ValueError: If the number of transactions is less than 1 or greater than the
                   number of possible transactions (n-1), where n is the length of
                   the stock prices list.
    """
    if k < 1:
        raise ValueError("Number of transactions must be at least 1.")
    n = len(stock_transactions)
    if k >= n - 1:
        raise ValueError("Maximum number of transactions exceeds allowed range.")

    # Initialize a DP table to keep track of maximum profit after each transaction
    dp = [[0] * (k+1) for _ in range(n)]
    max_profit = 0

    for i in range(n):
        max_profit = max(max_profit, dp[i][k-1])  # Current maximum

        for j in range(1, min(i, k)+1):  # Only consider up to min(i, k) transactions
            if i == j:
                # First transaction: buy on day 0, sell on day i
                dp[i][j] = max(dp[i-1][j], 
                               stock_transactions[i] - stock_transactions[0])
            else:
                # Subsequent transactions: carry forward the max profit
                dp[i][j] = max(dp[i-1][j], 
                               dp[i-1][j-1] + 
                               stock_transactions[i] - stock_transactions[i-j])

    return max_profit