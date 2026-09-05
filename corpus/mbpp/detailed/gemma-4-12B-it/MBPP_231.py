from typing import List

def max_sum(triangle: List[List[int]], n: int) -> int:
    """
    Finds the maximum path sum from the top of a triangle to the base.
    The path can only move to adjacent numbers in the row below.

    Args:
        triangle: A list of lists representing the triangular structure.
        n: The number of rows in the triangle.

    Returns:
        The maximum sum possible along a path from top to bottom.

    Raises:
        ValueError: If the input triangle structure is invalid.
    """
    # --- Input Validation ---
    if not isinstance(triangle, list) or not triangle:
        raise ValueError("Input triangle must be a non-empty list of lists.")

    if len(triangle) != n:
        raise ValueError(f"The triangle must have {n} rows, but received {len(triangle)}.")

    # Validate the triangular structure (each row i should have i+1 elements)
    for row_index, row in enumerate(triangle):
        if not isinstance(row, list):
            raise ValueError(f"Row {row_index} is not a list.")
        if len(row) != row_index + 1:
            raise ValueError(f"Row {row_index} has {len(row)} elements, expected {row_index + 1}.")
        for element in row:
            if not isinstance(element, (int, float)):
                raise ValueError(f"Triangle contains non-numeric value: {element}")

    # --- Edge Case Handling ---
    # If the triangle has only one row, the maximum sum is the value of that single element.
    if n == 1:
        return triangle[0][0]

    # --- Logic ---
    # We use a Bottom-Up Dynamic Programming approach.
    # The idea is to start from the second-to-last row and move upwards.
    # For each element in the current row, we add the maximum of its two children 
    # from the row below it.

    # Create a deep copy of the triangle to avoid mutating the input list.
    # We will use this copied structure to store the accumulated sums.
    dp_triangle = [list(row) for row in triangle]

    # Start from the row just above the bottom row (index n-2).
    # We iterate backwards towards the top of the triangle (index 0).
    for row_idx in range(n - 2, -1, -1):
        current_row = dp_triangle[row_idx]
        next_row = dp_triangle[row_idx + 1]

        for col_idx in range(len(current_row)):
            # The children of current_row[col_idx] are:
            # next_row[col_idx] and next_row[col_idx + 1]
            left_child = next_row[col_idx]
            right_child = next_row[col_idx + 1]

            # Determine the maximum contribution from the row below.
            max_child_sum = left_child if left_child > right_child else right_child

            # Update the current cell with the sum of itself and the max child.
            current_row[col_idx] = current_row[col_idx] + max_child_sum

    # After the loop finishes, dp_triangle[0][0] contains the maximum path sum.
    max_path_sum = dp_triangle[0][0]
    return int(max_path_sum) if isinstance(max_path_sum, float) and max_path_sum.is_integer() else max_path_sum