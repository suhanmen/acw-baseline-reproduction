def maximum_Sum(matrix):
    # Check if the input is valid
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Invalid input: matrix must be a list of lists")

    # Handle empty input
    if not matrix:
        return 0

    max_sum = -float('inf')  # Initialize to negative infinity

    for row in matrix:
        # Check if any row is empty
        if not isinstance(row, list) or len(row) == 0:
            current_sum = 0
        else:
            current_sum = sum(row)

        if current_sum > max_sum:
            max_sum = current_sum

    # After processing all rows, return the maximum sum found
    return max_sum if max_sum != -float('inf') else 0