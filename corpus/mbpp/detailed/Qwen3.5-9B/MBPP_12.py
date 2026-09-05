from typing import List, Union, Any

Number = Union[int, float]

def _validate_row(row: Any) -> bool:
    """
    Validate that a row is a non-empty list of numbers.
    Returns True if valid, False otherwise.
    """
    if not isinstance(row, list):
        return False

    if len(row) == 0:
        return False

    for element in row:
        if not isinstance(element, (int, float)):
            return False

    return True

def _validate_matrix(matrix: Any) -> bool:
    """
    Validate that the input is a matrix (list of rows) where:
    1. The matrix itself is a list.
    2. All rows in the matrix have the same length.
    3. All rows are non-empty lists of numbers.
    Returns True if valid, False otherwise.
    """
    if not isinstance(matrix, list):
        return False

    if len(matrix) == 0:
        return True  # Empty matrix is technically valid but produces empty output

    # Check if all rows exist and have the same length
    row_lengths = []
    for row in matrix:
        if not _validate_row(row):
            return False
        row_lengths.append(len(row))

    # Check that all rows have the same length
    expected_length = row_lengths[0]
    for length in row_lengths:
        if length != expected_length:
            return False

    return True

def _calculate_row_sum(row: List[Number]) -> Number:
    """
    Calculate the sum of all elements in a row.
    """
    total_sum = 0
    for value in row:
        total_sum += value
    return total_sum

def _sort_matrix_by_row_sum(matrix: List[List[Number]]) -> List[List[Number]]:
    """
    Create a deep copy of the matrix and sort its rows based on the sum of their elements.

    Steps:
    1. Create a copy of the input matrix to avoid modifying the original.
    2. Extract all row sums.
    3. Pair each row with its sum.
    4. Sort the pairs based on the sum.
    5. Extract the sorted rows from the pairs.
    6. Return the sorted matrix.
    """
    # Step 1: Create a deep copy of the matrix
    sorted_matrix_copy = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value)
        sorted_matrix_copy.append(new_row)

    # Step 2 & 3: Create a list of (row, sum) tuples
    row_sum_pairs = []
    for current_row in sorted_matrix_copy:
        current_sum = _calculate_row_sum(current_row)
        row_sum_pairs.append((current_row, current_sum))

    # Step 4: Sort the pairs based on the sum (ascending)
    # Using a custom key function for clarity
    row_sum_pairs.sort(key=lambda pair: pair[1])

    # Step 5: Extract the sorted rows
    final_sorted_matrix = []
    for pair in row_sum_pairs:
        final_sorted_matrix.append(pair[0])

    # Step 6: Return the result
    return final_sorted_matrix

def sort_matrix(matrix: Any) -> List[List[Number]]:
    """
    Sort a given matrix in ascending order according to the sum of its rows.

    Input Validation:
    - matrix must be a list.
    - matrix must not be empty unless explicitly allowed (empty list returns empty list).
    - Every element in matrix must be a list.
    - Every row must be non-empty.
    - Every row must contain only numbers (int or float).
    - All rows must have the same length.

    Returns:
    - A new matrix sorted by row sums.

    Raises:
    - ValueError: If the input matrix is invalid.
    """
    if not _validate_matrix(matrix):
        raise ValueError(
            "Invalid matrix input. The matrix must be a list of non-empty rows "
            "where all rows have the same length and contain only numeric values."
        )

    return _sort_matrix_by_row_sum(matrix)