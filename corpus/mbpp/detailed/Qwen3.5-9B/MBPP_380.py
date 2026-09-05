from typing import List, Union

def multi_list(rows: int, cols: int) -> List[List[int]]:
    """
    Generates a two-dimensional array (matrix) based on the provided row and column counts.

    The resulting matrix follows this specific pattern:
    - The first row (index 0) consists entirely of zeros.
    - The first column (index 0) of every row consists entirely of zeros.
    - For any cell at row index i (1 to rows-1) and column index j (1 to cols-1):
      value = i * j

    Args:
        rows (int): The number of rows in the resulting matrix. Must be a positive integer.
        cols (int): The number of columns in the resulting matrix. Must be a positive integer.

    Returns:
        List[List[int]]: A two-dimensional list representing the generated matrix.

    Raises:
        TypeError: If either 'rows' or 'cols' is not an integer or if they are not positive.
        ValueError: If either 'rows' or 'cols' is less than or equal to zero.
    """

    # Step 1: Validate input types explicitly
    if not isinstance(rows, int):
        raise TypeError(f"Expected 'rows' to be an integer, got {type(rows).__name__}")
    if not isinstance(cols, int):
        raise TypeError(f"Expected 'cols' to be an integer, got {type(cols).__name__}")

    # Step 2: Validate input values (boundary checks for degenerate cases)
    if rows <= 0 or cols <= 0:
        raise ValueError(f"Expected 'rows' and 'cols' to be positive integers. Got rows={rows}, cols={cols}.")

    # Step 3: Initialize the result structure
    # We pre-allocate the list to hold 'rows' lists.
    final_matrix: List[List[int]] = []

    # Helper function to create a single row to keep logic encapsulated and clean
    def create_row(row_index: int, col_count: int) -> List[int]:
        """
        Creates a single row for the matrix.

        Args:
            row_index (int): The 0-based index of the row (0, 1, 2, ...).
            col_count (int): The number of columns required.

        Returns:
            List[int]: A list representing the current row.
        """
        current_row: List[int] = []

        for col_index in range(col_count):
            # Logic: 
            # If the current row index is 0 (first row), the value is 0.
            # If the current column index is 0 (first column), the value is 0.
            # Otherwise, the value is row_index * col_index.

            if row_index == 0 or col_index == 0:
                cell_value: int = 0
            else:
                cell_value: int = row_index * col_index

            current_row.append(cell_value)

        return current_row

    # Step 4: Populate the matrix row by row
    for current_row_idx in range(rows):
        # Generate the specific row for this index and append to the final matrix
        generated_row: List[int] = create_row(current_row_idx, cols)
        final_matrix.append(generated_row)

    # Step 5: Return the completed matrix
    return final_matrix