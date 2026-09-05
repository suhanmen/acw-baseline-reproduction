def max_sum(triangle, num_steps):
    """
    Find the maximum sum in the given right triangle of numbers.

    Args:
        triangle: A list of lists where each sublist represents a row in the triangle.
        num_steps: An integer representing the number of steps to take from the top.

    Returns:
        The maximum sum possible after taking num_steps from the top.

    Raises:
        ValueError: If the input is invalid (e.g., empty triangle, incorrect row lengths).
    """
    # Validate the triangle
    if not triangle:
        raise ValueError("The triangle cannot be empty.")
    for row in triangle:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError("Each row must be a non-empty list.")

    # Check if the triangle is properly formed
    expected_length = len(triangle[0]) + num_steps - 1
    if len(triangle[-1]) != expected_length:
        raise ValueError("The last row has incorrect length based on the number of steps.")

    # Initialize a DP table
    dp = [row[:] for row in triangle]

    # Fill the DP table
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                # Only can come from above
                dp[i][j] += dp[i-1][j]
            elif j == i:
                # Can come from above-left or above-right (but in our case, only above is possible)
                dp[i][j] += dp[i-1][j-1]
            else:
                # Can come from above-left or above
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    # Get the last row and find the maximum value
    last_row = dp[-1]
    return max(last_row)