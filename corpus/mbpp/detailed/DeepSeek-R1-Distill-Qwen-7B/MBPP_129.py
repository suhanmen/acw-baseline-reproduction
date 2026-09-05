def magic_square(matrix):
    """
    Check if the given matrix is a magic square.
    A magic square is a square grid where the sum of the numbers in each row,
    each column, and both main diagonals are the same.

    Args:
        matrix (list of lists): The square matrix to check.

    Returns:
        bool: True if it is a magic square, False otherwise.

    Raises:
        ValueError: If the matrix is not a square matrix.
    """
    # Check if the matrix is a square matrix
    rows = len(matrix)
    if rows == 0:
        raise ValueError("Matrix must have at least one row.")
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise ValueError("Matrix is not a square matrix.")

    # Collect row sums
    row_sums = []
    for row in matrix:
        row_sum = sum(row)
        row_sums.append(row_sum)

    # Collect column sums
    col_sums = []
    for c in range(cols):
        col_sum = 0
        for r in range(rows):
            col_sum += matrix[r][c]
        col_sums.append(col_sum)

    # Check diagonals
    diag1_sum = sum(matrix[i][i] for i in range(rows))
    diag2_sum = sum(matrix[i][cols - 1 - i] for i in range(rows))

    # Collect all sums
    all_sums = row_sums + col_sums + [diag1_sum, diag2_sum]

    # Check if all sums are equal
    first_sum = all_sums[0]
    for s in all_sums[1:]:
        if s != first_sum:
            return False

    return True