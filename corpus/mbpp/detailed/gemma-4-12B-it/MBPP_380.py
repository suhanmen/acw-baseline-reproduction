from typing import List

def multi_list(rows: int, cols: int) -> List[List[int]]:
    """
    Generates a two-dimensional array (list of lists) where each element 
    at position (i, j) is the result of the multiplication of the row 
    index i and the column index j.

    Args:
        rows (int): The number of rows in the resulting grid.
        cols (int): The number of columns in the resulting grid.

    Returns:
        List[List[int]]: A 2D list of size rows x cols.

    Raises:
        ValueError: If rows or cols are negative.
        TypeError: If rows or cols are not integers.
    """
    # Validate input types
    if not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError("Both 'rows' and 'cols' must be integers.")

    # Validate input ranges
    if rows < 0 or cols < 0:
        raise ValueError("Dimensions 'rows' and 'cols' must be non-negative.")

    # Handle the edge case where rows or cols are zero
    # The result should be an empty list (if rows=0) or a list of empty lists (if cols=0)
    if rows == 0:
        return []
    if cols == 0:
        return [[] for _ in range(rows)]

    # Initialize the outer container
    result_grid: List[List[int]] = []

    # Iterate through each row index
    for row_idx in range(rows):
        # Create a temporary list for the current row
        current_row: List[int] = []

        # Iterate through each column index
        for col_idx in range(cols):
            # Calculate the value: row_index * column_index
            # Example: row 2, col 3 -> 2 * 3 = 6
            value = row_idx * col_idx

            # Append the calculated value to the current row
            current_row.append(value)

        # Append the completed row to the result grid
        result_grid.append(current_row)

    return result_grid

# Verification against provided assertions
if __name__ == "__main__":
    # Test Case 1
    assert multi_list(3, 4) == [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

    # Test Case 2
    assert multi_list(5, 7) == [
        [0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 2, 3, 4, 5, 6], 
        [0, 2, 4, 6, 8, 10, 12], 
        [0, 3, 6, 9, 12, 15, 18], 
        [0, 4, 8, 12, 16, 20, 24]
    ]

    # Test Case 3
    expected_10_15 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 
        [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28], 
        [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42], 
        [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56], 
        [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70], 
        [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84], 
        [0, 7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98], 
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112], 
        [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108, 117, 126]
    ]
    assert multi_list(10, 15) == expected_10_15