from typing import List


def sort_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Sorts a matrix such that the rows are ordered by their sum in ascending order.

    Args:
        matrix (List[List[int]]): A 2D list of integers.

    Returns:
        List[List[int]]: A new 2D list sorted by row sums.

    Raises:
        ValueError: If the input is not a list of lists or if row lengths are inconsistent.
        TypeError: If elements are not integers.
    """
    # 1. Validate input type
    if not isinstance(matrix, list):
        raise TypeError("Input must be a list of lists.")

    # 2. Handle empty matrix case
    if not matrix:
        return []

    # 3. Check for consistent row lengths and types
    # We perform this check upfront to ensure data integrity
    first_row_length = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("Each element in the matrix must be a list.")

        current_row_length = len(row)
        if first_row_length is None:
            first_row_length = current_row_length
        elif current_row_length != first_row_length:
            raise ValueError("All rows in the matrix must have the same length.")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("All elements in the matrix must be numbers.")

    # 4. Helper function to calculate row sum
    def calculate_row_sum(row: List[int]) -> int:
        total = 0
        for value in row:
            total += value
        return total

    # 5. Create a list of tuples (row_sum, original_row)
    # We use tuples to keep the original row associated with its calculated sum.
    # This prevents recalculating the sum multiple times during the sort process.
    indexed_rows = []
    for row in matrix:
        row_sum = calculate_row_sum(row)
        indexed_rows.append((row_sum, row))

    # 6. Sort the list of tuples
    # Python's sort is stable, which preserves order for rows with identical sums.
    # We sort based on the first element of the tuple (the sum).
    indexed_rows.sort(key=lambda x: x[0])

    # 7. Extract the sorted rows from the tuples
    sorted_matrix = []
    for item in indexed_rows:
        sorted_matrix.append(item[1])

    return sorted_matrix


# Manual verification of the requested assertions
if __name__ == "__main__":
    # Test Case 1
    case1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
    # Sums: 6, 11, 3 -> Expected order sums: 3, 6, 11
    assert sort_matrix(case1) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

    # Test Case 2
    case2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
    # Sums: 6, -3, 1 -> Expected order sums: -3, 1, 6
    assert sort_matrix(case2) == [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]

    # Test Case 3
    case3 = [[5, 8, 9], [6, 4, 3], [2, 1, 4]]
    # Sums: 22, 13, 7 -> Expected order sums: 7, 13, 22
    assert sort_matrix(case3) == [[2, 1, 4], [6, 4, 3], [5, 8, 9]]