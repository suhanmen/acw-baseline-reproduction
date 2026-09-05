from typing import List


def max_profit(prices: List[int], k: int) -> int:
    """
    Calculates the maximum profit that can be achieved from at most k transactions.
    A transaction consists of buying a stock and selling it later.

    Args:
        prices: A list of integers representing the stock prices on consecutive days.
        k: The maximum number of transactions allowed.

    Returns:
        The maximum profit possible.

    Raises:
        ValueError: If prices is empty or k is negative.
    """
    # --- Input Validation ---
    if not isinstance(prices, list):
        raise ValueError("Input 'prices' must be a list of integers.")

    if not isinstance(k, int) or k < 0:
        raise ValueError("Input 'k' must be a non-negative integer.")

    # Edge case: No prices provided or no transactions allowed
    if not prices or k == 0:
        return 0

    num_days = len(prices)

    # Optimization: If k is large enough to cover every possible profitable transaction,
    # we can treat this as an unlimited transactions problem (Greedy approach).
    # A transaction requires at least 2 days (buy and sell).
    if k >= num_days // 2:
        return _calculate_unlimited_profit(prices)

    # --- Dynamic Programming Approach ---
    # We use a DP table where:
    # dp[i][j] = max profit using at most i transactions up to day j.

    # Initialize a 2D table with 0s
    # Rows: transactions from 0 to k (k+1 rows)
    # Columns: days from 0 to num_days-1 (num_days columns)
    dp = [[0 for _ in range(num_days)] for _ in range(k + 1)]

    # Iterate through the number of allowed transactions
    for i in range(1, k + 1):
        # max_diff tracks the maximum of (dp[i-1][m] - prices[m])
        # which represents the profit from previous transactions minus the cost 
        # to buy the stock on day m.
        max_diff = -float('inf')

        for j in range(num_days):
            # Update max_diff: 
            # We consider the best day 'm' (where m < j) to have bought the stock.
            # The profit would be (profit from i-1 transactions at day m) - (price at day m).
            # Since we update this iteratively, we check the profit from the previous 
            # transaction count at the previous day.
            current_buy_profit = dp[i - 1][j] - prices[j]
            if current_buy_profit > max_diff:
                max_diff = current_buy_profit

            # The max profit at day j with i transactions is the maximum of:
            # 1. Not doing anything on day j (profit remains same as day j-1)
            # 2. Selling the stock on day j that was bought at the best possible day.
            profit_if_sold_today = prices[j] + max_diff

            # If we are on the first day, profit_if_sold_today might be based on -inf.
            # We ensure we don't pick a negative profit by comparing with 0 or the previous day.
            if j > 0:
                if profit_if_sold_today > dp[i][j - 1]:
                    dp[i][j] = profit_if_sold_today
                else:
                    dp[i][j] = dp[i][j - 1]
            else:
                # On day 0, profit is always 0 because you can't sell what you haven't bought.
                dp[i][j] = 0

    return int(dp[k][num_days - 1])


def _calculate_unlimited_profit(prices: List[int]) -> int:
    """
    Helper function to calculate profit with unlimited transactions.
    This is used as an optimization when k >= num_days // 2.
    """
    total_profit = 0
    for i in range(1, len(prices)):
        # If the price today is higher than yesterday, "sell" today.
        # This effectively captures every upward price movement.
        if prices[i] > prices[i - 1]:
            total_profit += (prices[i] - prices[i - 1])
    return total_profit