def max_path_sum(triangle, row, col):
    # Create a 2D list to store the maximum path sums
    dp = [[0 for _ in range(len(row))] for row in triangle]

    # Initialize the last row of dp with the values from the triangle
    dp[-1] = triangle[-1]

    # Iterate from the second last row to the first row
    for i in range(len(triangle)-2, -1, -1):
        # Iterate through each element in the current row
        for j in range(len(triangle[i])):
            # Calculate the maximum path sum for the current element
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

    # Return the maximum value in the dp table, which is the maximum total path sum
    return max(dp)