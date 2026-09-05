from typing import List


def max_path_sum(triangle: List[List[int]], rows: int, cols: int) -> int:
    """
    Finds the maximum total path sum in a triangle of numbers.

    The path starts at the top vertex and moves to adjacent numbers in the row below.
    A number at index [i][j] can move to [i+1][j] or [i+1][j+1].

    Args:
        triangle: A 2D list of integers representing the triangle.
        rows: The number of rows in the triangle.
        cols: The number of columns in the bottom row (or max width).

    Returns:
        The maximum path sum from top to bottom.

    Raises:
        ValueError: If input dimensions are invalid or triangle structure is incorrect.
    """
    # --- Input Validation ---
    if not isinstance(triangle, list) or not triangle:
        raise ValueError("Triangle must be a non-empty list of lists.")

    if rows <= 0 or cols <= 0:
        raise ValueError("Dimensions rows and cols must be positive integers.")

    # Validate the structure of the triangle
    # A triangle with 'rows' rows should have each row 'i' have at least 'i+1' elements
    # and the bottom row should have 'rows' elements (or up to 'cols').
    for i in range(rows):
        if i >= len(triangle):
            raise ValueError(f"Triangle has fewer than {rows} rows.")

        current_row = triangle[i]
        if not isinstance(current_row, list):
            raise ValueError(f"Row {i} is not a list.")

        # Check if the row has enough elements to satisfy triangle properties
        # Usually, row i has i+1 elements. 
        if len(current_row) < (i + 1):
            raise ValueError(f"Row {i} has insufficient elements for a triangle structure.")

    # --- Edge Case Handling ---
    # If there is only one row, the max path sum is the value of that single element.
    if rows == 1:
        return triangle[0][0]

    # --- Algorithm Logic ---
    # We use Dynamic Programming (Bottom-Up approach).
    # The idea is to start from the second-to-last row and work upwards.
    # For each element, we add the maximum of the two reachable elements below it.

    # Create a copy of the triangle to avoid mutating the original input.
    # This ensures our function is side-effect free (defensive programming).
    dp_table = [row[:] for row in triangle]

    # Start from the row above the bottom row
    # Row index starts at 0, so the bottom row is rows - 1.
    # We iterate from row index 'rows - 2' down to 0.
    for current_row_idx in range(rows - 2, -1, -1):
        # Process each element in the current row
        for current_col_idx in range(len(dp_table[current_row_idx])):

            # The two possible paths from triangle[current_row_idx][current_col_idx]
            # are to the elements directly below it and to its bottom-right.
            # These are at:
            # 1. [current_row_idx + 1][current_col_idx]
            # 2. [current_row_idx + 1][current_col_idx + 1]

            # Note: Because of the triangle property, the element at 
            # [current_row_idx + 1][current_col_idx + 1] is guaranteed 
            # to exist because the row below has more elements.

            below_left = dp_table[current_row_idx + 1][current_col_idx]
            below_right = dp_table[current_row_idx + 1][current_col_idx + 1]

            # Select the maximum of the two paths available from the row below
            max_from_below = max(below_left, below_right)

            # Update the current cell with the sum of itself and the best path below
            dp_table[current_row_idx][current_col_idx] += max_from_below

    # The result is stored at the top of our DP table
    final_result = dp_table[0][0]

    return final_result