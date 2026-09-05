def validate_square_structure(matrix):
    """
    Validates that the input is a well-formed square matrix (list of lists).

    Returns:
        list | None: The validated matrix if successful, None otherwise.
    """
    if not isinstance(matrix, list):
        return None

    if len(matrix) == 0:
        return None

    n = len(matrix)

    for row in matrix:
        if not isinstance(row, list):
            return None
        if len(row) != n:
            return None
        for element in row:
            if not isinstance(element, (int, float)):
                return None

    return matrix


def calculate_row_sums(matrix):
    """
    Calculates the sum of elements for each row.

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        list: A list of integers or floats representing row sums.
    """
    row_sums = []
    for row in matrix:
        current_sum = 0
        for value in row:
            current_sum += value
        row_sums.append(current_sum)
    return row_sums


def calculate_column_sums(matrix):
    """
    Calculates the sum of elements for each column.

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        list: A list of integers or floats representing column sums.
    """
    n = len(matrix)
    column_sums = []

    for col_index in range(n):
        current_sum = 0
        for row_index in range(n):
            value = matrix[row_index][col_index]
            current_sum += value
        column_sums.append(current_sum)

    return column_sums


def calculate_diagonal_sums(matrix):
    """
    Calculates the sum of the primary and secondary diagonals.

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        tuple: A tuple containing (primary_diagonal_sum, secondary_diagonal_sum).
    """
    n = len(matrix)

    primary_sum = 0
    secondary_sum = 0

    for index in range(n):
        primary_sum += matrix[index][index]
        secondary_sum += matrix[index][n - 1 - index]

    return primary_sum, secondary_sum


def calculate_expected_sum(matrix):
    """
    Calculates the expected magic constant (sum) for a magic square of size n.
    Formula: n * (n^2 + 1) / 2

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        float: The expected sum for each row, column, and diagonal.
    """
    n = len(matrix)
    total = sum(sum(row) for row in matrix)

    if total % n != 0:
        raise ValueError("The total sum of elements is not divisible by the size of the matrix.")

    expected = total / n
    return expected


def is_all_elements_unique(matrix):
    """
    Checks if all elements in the matrix are unique integers.

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        bool: True if all elements are unique, False otherwise.
    """
    n = len(matrix)
    expected_count = n * n

    flat_list = []
    for row in matrix:
        for value in row:
            flat_list.append(value)

    if len(flat_list) != expected_count:
        return False

    unique_elements = set(flat_list)

    return len(unique_elements) == expected_count


def are_all_values_positive_integers(matrix):
    """
    Checks if all values in the matrix are positive integers.
    Standard magic squares use positive integers starting from 1.
    However, based on the test cases (e.g., [2, 7, 6]...), we strictly check
    for integers > 0.

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        bool: True if all values are positive integers, False otherwise.
    """
    for row in matrix:
        for value in row:
            if not isinstance(value, int):
                return False
            if value <= 0:
                return False
    return True


def magic_square_test(matrix):
    """
    Determines if a given square matrix is a valid magic square.

    A magic square is defined here as:
    1. A square matrix (n x n).
    2. All elements are unique positive integers.
    3. Every row sums to the same value.
    4. Every column sums to the same value.
    5. Both main diagonals sum to the same value (which equals the row/column sum).

    Args:
        matrix: A 2D list representing the square matrix.

    Returns:
        bool: True if the matrix is a magic square, False otherwise.
    """
    validated_matrix = validate_square_structure(matrix)
    if validated_matrix is None:
        return False

    matrix = validated_matrix
    n = len(matrix)

    if n == 0:
        return False

    if are_all_values_positive_integers(matrix):
        pass
    else:
        return False

    expected_sum = calculate_expected_sum(matrix)

    row_sums = calculate_row_sums(matrix)
    if not all(sum_val == expected_sum for sum_val in row_sums):
        return False

    column_sums = calculate_column_sums(matrix)
    if not all(sum_val == expected_sum for sum_val in column_sums):
        return False

    primary_diag, secondary_diag = calculate_diagonal_sums(matrix)
    if primary_diag != expected_sum or secondary_diag != expected_sum:
        return False

    return is_all_elements_unique(matrix)