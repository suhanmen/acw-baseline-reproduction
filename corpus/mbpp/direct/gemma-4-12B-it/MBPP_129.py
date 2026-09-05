def magic_square_test(matrix):
    """
    Checks if a given 2D list is a magic square.
    A magic square is a square matrix where the sum of each row,
    each column, and both main diagonals are equal.
    Also, all numbers in the matrix must be unique.
    """
    if not matrix or not matrix[0]:
        return False

    n = len(matrix)
    # Check if it is a square matrix
    for row in matrix:
        if len(row) != n:
            return False

    # Check if all elements are unique
    flat_list = [item for row in matrix for item in row]
    if len(set(flat_list)) != n * n:
        return False

    # Calculate the target sum (sum of the first row)
    target_sum = sum(matrix[0])

    # Check rows
    for row in matrix:
        if sum(row) != target_sum:
            return False

    # Check columns
    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != target_sum:
            return False

    # Check main diagonal (top-left to bottom-right)
    diag1_sum = sum(matrix[i][i] for i in range(n))
    if diag1_sum != target_sum:
        return False

    # Check anti-diagonal (top-right to bottom-left)
    diag2_sum = sum(matrix[i][n - 1 - i] for i in range(n))
    if diag2_sum != target_sum:
        return False

    return True