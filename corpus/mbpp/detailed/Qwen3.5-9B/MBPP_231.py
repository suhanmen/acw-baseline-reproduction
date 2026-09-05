from typing import List, Union

Number = Union[int, float]

def _validate_input(data: List[List[Number]], n: Number) -> None:
    """
    Validate the input arguments for the max_sum function.

    Checks:
    - n is an integer and n > 0.
    - data is a non-empty list.
    - data has exactly n rows.
    - Each row i (0-indexed) has exactly i + 1 elements.
    - All elements in the triangle are numbers (int or float).
    """
    # Validate n
    if not isinstance(n, int):
        raise TypeError(f"The parameter 'n' must be an integer, got {type(n).__name__}.")

    if n <= 0:
        raise ValueError(f"The parameter 'n' must be a positive integer, got {n}.")

    # Validate data is a list
    if not isinstance(data, list):
        raise TypeError(f"The parameter 'data' must be a list of lists, got {type(data).__name__}.")

    if len(data) == 0:
        raise ValueError(f"The parameter 'data' cannot be an empty list, expected {n} rows.")

    # Check row count
    if len(data) != n:
        raise ValueError(f"The parameter 'data' must have exactly {n} rows, got {len(data)}.")

    # Check structure of each row and element types
    for row_index in range(n):
        current_row = data[row_index]

        # Check if current row is a list
        if not isinstance(current_row, list):
            raise TypeError(f"Row {row_index} must be a list, got {type(current_row).__name__}.")

        expected_length = row_index + 1
        actual_length = len(current_row)

        if actual_length != expected_length:
            raise ValueError(
                f"Row {row_index} must have {expected_length} elements (forming a triangle), "
                f"got {actual_length} elements."
            )

        # Check element types in the current row
        for element_index, value in enumerate(current_row):
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Element at row {row_index}, column {element_index} must be a number, "
                    f"got {type(value).__name__}."
                )

def _get_subtriangle_elements(data: List[List[Number]], max_level: int) -> List[Number]:
    """
    Extracts elements from the top-left sub-triangle of height 'max_level'.

    In a right-angled triangle represented as:
    Row 0: [a0]
    Row 1: [a1, a2]
    Row 2: [a3, a4, a5]

    If we limit to 'max_level', we take rows 0 to max_level-1.
    However, looking at the problem context (finding max sum in a 'right triangle'),
    usually implies finding the maximum path sum from top to bottom where you can move
    down-left or down-right. This is the classic Triangle Problem (Project Euler #18 style).

    The problem signature includes 'n', which matches the number of rows.
    The examples show standard triangle structures.
    We will calculate the maximum path sum from the top element to the bottom row.
    """
    # We will copy the data slightly to avoid mutating input if that matters, 
    # though for this logic just reading is fine.
    # We limit processing to the first 'n' rows (which is the whole input based on validation).

    triangle_rows = []
    for i in range(n):
        triangle_rows.append(data[i])

    # Create a DP table to store maximum path sum to reach each element
    # dp[row][col] = max sum to reach triangle_rows[row][col]
    dp_table = []

    # Initialize first row
    first_row_data = triangle_rows[0]
    first_row_dp = [first_row_data[0]]
    dp_table.append(first_row_dp)

    # Process subsequent rows
    for row_index in range(1, n):
        current_row_data = triangle_rows[row_index]
        current_row_dp = []

        for col_index in range(len(current_row_data)):
            value = current_row_data[col_index]

            # From the top (row - 1), we could have come from:
            # 1. The element directly above-left: (row-1, col-1) -> valid if col > 0
            # 2. The element directly above-right: (row-1, col) -> valid if col < len(prev_row)

            candidates = []

            # Check upper-left parent
            if col_index > 0:
                parent_sum = dp_table[row_index - 1][col_index - 1]
                candidates.append(parent_sum)

            # Check upper-right parent
            # In a standard triangle layout:
            # Row i-1 has indices 0 to i-1
            # Row i has indices 0 to i
            # Index 'col' in row 'i' connects to 'col' in row 'i-1' (upper-left relative to visual slope often)
            # Let's trace the example:
            # [[1], [2,1], [3,3,2]]
            # To reach [1] in row 1 (index 1): comes from [1] in row 0 (index 0).
            # To reach [2] in row 1 (index 0): comes from [1] in row 0 (index 0).
            # Generally, element (r, c) can come from (r-1, c-1) and (r-1, c).

            if col_index < len(dp_table[row_index - 1]):
                parent_sum = dp_table[row_index - 1][col_index]
                candidates.append(parent_sum)

            # Find max parent sum
            if len(candidates) == 0:
                # This case should not happen in a valid triangle for col_index >= 0
                # unless n=0, but n is validated > 0.
                # Fallback for safety (should not be reached)
                current_sum = value
            else:
                max_parent = max(candidates)
                current_sum = max_parent + value

            current_row_dp.append(current_sum)

        dp_table.append(current_row_dp)

    # The result is the maximum value in the last row of the DP table
    if len(dp_table) == 0:
        return 0

    last_row_dp = dp_table[-1]
    result = max(last_row_dp)

    return result

def max_sum(data: List[List[Number]], n: Number) -> Number:
    """
    Finds the maximum sum path from the top to the bottom of a given number triangle.

    The triangle is represented as a list of lists, where the i-th list has i+1 elements.
    From any element in row 'r', you can move to either the element directly below-left
    or directly below-right in row 'r+1'. The goal is to find the path from the top
    element to the bottom row that maximizes the sum of numbers along the path.

    Args:
        data: A list of lists representing the triangle of numbers.
        n: The number of rows in the triangle (must be equal to len(data)).

    Returns:
        The maximum sum achievable from the top to the bottom of the triangle.

    Raises:
        TypeError: If inputs are not lists, integers, or numbers as required.
        ValueError: If n is non-positive or data structure is invalid.
    """
    # Step 1: Validate inputs explicitly
    _validate_input(data, n)

    # Step 2: Determine the range of rows to process
    # Based on validation, len(data) == n. We process all rows.
    rows_to_process = n

    # Step 3: Helper to extract and compute max path
    # We reuse the logic from _get_subtriangle_elements but make it self-contained 
    # within max_sum or call the helper. Let's use the helper for clarity as requested.
    max_value = _get_subtriangle_elements(data, rows_to_process)

    return max_value