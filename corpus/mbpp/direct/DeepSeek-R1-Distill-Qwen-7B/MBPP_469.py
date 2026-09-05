def max_profit(prices, k):
    if k == 0 or not prices:
        return 0

    profit = [[0] * (k + 1) for _ in range(len(prices))]
    for i in range(1, len(prices)):
        buy = 0
        for j in range(1, min(i, k) + 1):
            if j == 1:
                buy = -prices[i]
            else:
                buy = max(profit[i-1][j-1] - prices[i], buy)
        for j in range(1, k + 1):
            if j == 1:
                profit[i][j] = max(profit[i-1][j], prices[i] - prices[i-1])
            else:
                profit[i][j] = max(profit[i-1][j], profit[i-1][j-1] + prices[i] - prices[i-1])

    return profit[-1][k]