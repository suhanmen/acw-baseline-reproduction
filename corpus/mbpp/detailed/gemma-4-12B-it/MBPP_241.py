from typing import List

def array_3d(depth: int, rows: int, cols: int) -> List[List[List[str]]]:
    """
    Generates a 3D array (list of lists of lists) filled with the '*' character.

    The dimensions are:
    - depth: The number of 2D matrices in the outer list.
    - rows: The number of rows in each 2D matrix.
    - cols: The number of columns in each row.

    Args:
        depth (int): The number of 2D matrices.
        rows (int): The number of rows per matrix.
        cols (int): The number of columns per row.

    Returns:
        List[List[List[str]]]: A 3D array structure filled with '*'.

    Raises:
        ValueError: If any dimension is negative.
        TypeError: If any dimension is not an integer.
    """

    # Validate input types
    if not isinstance(depth, int) or not isinstance(rows, int) or not isinstance(cols, int):
        raise TypeError("All dimensions (depth, rows, cols) must be integers.")

    # Validate input values (dimensions cannot be negative)
    if depth < 0 or rows < 0 or cols < 0:
        raise ValueError("All dimensions must be non-negative integers.")

    # Handle the edge case where any dimension is zero.
    # Depending on the specific interpretation, a 0-dimension array 
    # might be an empty list or a list of empty lists.
    # Following standard nested list conventions, we create the structures accordingly.
    if depth == 0:
        return []

    # We use a nested list comprehension or explicit loops to ensure 
    # that each inner list is a unique object in memory.
    # If we used [[*] * cols] * rows, modifying one row would modify all rows.

    result_3d = []

    for d_idx in range(depth):
        # Initialize the 2D matrix for the current depth level
        matrix_2d = []

        for r_idx in range(rows):
            # Initialize the 1D row for the current row index
            row_1d = []

            for c_idx in range(cols):
                # Append the character to the row
                row_1d.append('*')

            # Add the completed row to the 2D matrix
            matrix_2d.append(row_1d)

        # Add the completed 2D matrix to the 3D structure
        result_3d.append(matrix_2d)

    return result_3d