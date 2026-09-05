import math

def get_Min_Squares(n):
    if n <= 1:
        return n

    # Precompute squares up to sqrt(n)
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    # dp[i] will store the minimum number of squares that sum to i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for sq in squares:
            if sq > i:
                break
            dp[i] = min(dp[i], dp[i - sq] + 1)

    return dp[n]