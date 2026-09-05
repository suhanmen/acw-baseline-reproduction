def max_sum(triangle, n):
    """
    Finds the maximum path sum from top to bottom in a triangle of numbers.
    The path can move to adjacent numbers in the row below.
    """
    # Create a copy to avoid modifying the original list
    dp = [row[:] for row in triangle]

    # Start from the second to last row and move upwards
    for i in range(n - 2, -1, -1):
        for j in range(len(dp[i])):
            # The max sum at dp[i][j] is the value itself plus the 
            # maximum of the two values directly below it
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]

if __name__ == "__main__":
    assert max_sum([[1], [2,1], [3,3,2]], 3) == 6
    assert max_sum([[1], [1, 2], [4, 1, 12]], 3) == 15 
    assert max_sum([[2], [3,2], [13,23,12]], 3) == 28