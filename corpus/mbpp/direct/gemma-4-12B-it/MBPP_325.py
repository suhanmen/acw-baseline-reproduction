def get_Min_Squares(n: int) -> int:
    """
    Finds the minimum number of perfect squares that sum up to a given number n.
    This is solved using dynamic programming.
    """
    # dp[i] will store the minimum number of squares that sum to i
    # Initialize dp table with infinity, except for dp[0] which is 0.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Pre-calculate all squares less than or equal to n
    squares = []
    i = 1
    while i * i <= n:
        squares.append(i * i)
        i += 1

    # Fill the dp table
    for i in range(1, n + 1):
        for square in squares:
            if square > i:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)

    return int(dp[n])

if __name__ == "__main__":
    assert get_Min_Squares(6) == 3
    assert get_Min_Squares(2) == 2
    assert get_Min_Squares(4) == 1