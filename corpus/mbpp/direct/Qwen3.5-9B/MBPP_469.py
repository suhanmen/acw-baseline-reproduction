from typing import List

def max_profit(prices: List[int], k: int) -> int:
    if not prices or k == 0 or len(prices) < 2:
        return 0

    n = len(prices)
    if k >= n // 2:
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    # buy[j] = max profit with at most j transactions and currently holding a stock
    # sell[j] = max profit with at most j transactions and not holding a stock
    buy = [float('-inf')] * (k + 1)
    sell = [0] * (k + 1)

    for price in prices:
        for j in range(1, k + 1):
            buy[j] = max(buy[j], sell[j - 1] - price)
            sell[j] = max(sell[j], buy[j] + price)

    return sell[k]