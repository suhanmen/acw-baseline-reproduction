from typing import List

def is_magic_square(matrix: List[List[int]]) -> bool:
    """
    Validates whether a given 2D list of integers represents a magic square.
    A magic square is a square matrix where the sum of every row, 
    every column, and both main diagonals are equal.

    Additionally, in a strict magic square definition, the matrix should 
    contain distinct numbers (usually 1 to n^2), but based on the 
    provided assertions, we focus on the sum equality.
    """

    # 1. Validate input type and structure
    if not isinstance(matrix, list) or not matrix:
        return False

    row_count = len(matrix)

    # Check if every row is a list
    for row in matrix:
        if not isinstance(row, list):
            return False

    # Check if the matrix is square (number of columns must equal row_count)
    for row in matrix:
        if len(row) != row_count:
            return False

    # Handle the case of an empty square (0x0) - though caught by 'not matrix'
    if row_count == 0:
        return False

    # 2. Calculate the reference sum (sum of the first row)
    # All other sums must match this value.
    first_row = matrix[0]
    target_sum = 0
    for value in first_row:
        if not isinstance(value, (int, float)):
            return False
        target_sum += value

    # 3. Verify all row sums
    for r_idx in range(row_count):
        current_row_sum = 0
        for c_idx in range(row_count):
            current_row_sum += matrix[r_idx][c_idx]

        if current_row_sum != target_sum:
            return False

    # 4. Verify all column sums
    for c_idx in range(row_count):
        current_col_sum = 0
        for r_idx in range(row_count):
            current_col_sum += matrix[r_idx][c_idx]

        if current_col_sum != target_sum:
            return False

    # 5. Verify main diagonal sum (top-left to bottom-right)
    main_diagonal_sum = 0
    for i in range(row_count):
        main_diagonal_sum += matrix[i][i]

    if main_diagonal_sum != target_sum:
        return False

    # 6. Verify anti-diagonal sum (top-right to bottom-left)
    anti_diagonal_sum = 0
    for i in range(row_count):
        # The column index is (row_count - 1 - current_row_index)
        anti_diagonal_sum += matrix[i][row_count - 1 - i]

    if anti_diagonal_sum != target_sum:
        return False

    # All checks passed
    return True

def magic_square_test(matrix: List[List[int]]) -> bool:
    """
    Wrapper function to satisfy the specific assertion signature provided.
    """
    return is_magic_square(matrix)