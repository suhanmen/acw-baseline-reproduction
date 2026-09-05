from typing import List, Union

Number = Union[int, float]

def max_path_sum(triangle: List[List[Number]], row_start: int, row_end: int) -> Number:
    """
    Computes the maximum path sum within a specified range of rows in a triangle.

    The triangle is represented as a list of lists, where each inner list corresponds to a row.
    The path starts at any element in the specified starting row and ends at any element
    in the specified ending row. Movement is restricted to moving to adjacent elements
    in the next row (i.e., from index i in row r, one can go to index i or i+1 in row r+1).

    Parameters:
    - triangle: A list of lists of numbers representing the triangle.
    - row_start: The starting row index (inclusive) within the triangle.
    - row_end: The ending row index (inclusive) within the triangle.

    Returns:
    - The maximum path sum found within the specified row range.

    Raises:
    - ValueError: If inputs are invalid (e.g., empty triangle, invalid row indices).
    - TypeError: If input types are incorrect.
    """

    # Step 1: Input Validation
    # Check if the triangle itself is a list
    if not isinstance(triangle, list):
        raise TypeError("The triangle must be a list.")

    # Check for empty triangle
    if len(triangle) == 0:
        raise ValueError("The triangle cannot be empty.")

    # Validate that every row in the triangle is a list
    for i, row in enumerate(triangle):
        if not isinstance(row, list):
            raise TypeError(f"Row at index {i} must be a list.")
        if len(row) != i + 1:
            raise ValueError(f"Row at index {i} must have exactly {i + 1} elements (found {len(row)}).")

    # Check if row_start and row_end are integers
    if not isinstance(row_start, int) or not isinstance(row_end, int):
        raise TypeError("row_start and row_end must be integers.")

    # Validate row indices against triangle dimensions
    num_rows = len(triangle)

    if row_start < 0 or row_start > num_rows - 1:
        raise ValueError(f"row_start ({row_start}) is out of bounds for a triangle with {num_rows} rows (valid: 0 to {num_rows - 1}).")

    if row_end < 0 or row_end > num_rows - 1:
        raise ValueError(f"row_end ({row_end}) is out of bounds for a triangle with {num_rows} rows (valid: 0 to {num_rows - 1}).")

    if row_start > row_end:
        raise ValueError(f"row_start ({row_start}) cannot be greater than row_end ({row_end}).")

    # Step 2: Define Helper Function to Calculate Maximum Path Sum in a Sub-triangle
    def solve_subtriangle(rows: List[List[Number]], start_row_idx: int, end_row_idx: int) -> Number:
        """
        Recursively or iteratively solves for the max path sum in a sub-triangle.
        Using Dynamic Programming (Bottom-Up approach for efficiency).

        We will work from the last row of the sub-triangle up to the first row.
        """
        # Extract the relevant slice of rows for this specific problem instance
        sub_triangle = rows[start_row_idx:end_row_idx + 1]

        # Base Case: If there is only one row in the sub-triangle
        if len(sub_triangle) == 1:
            single_row = sub_triangle[0]
            # Find the maximum value in that single row
            max_val = float('-inf')
            for val in single_row:
                if val > max_val:
                    max_val = val
            return max_val

        # Initialize DP table with the last row of our sub-triangle
        # The DP table size will match the number of rows in the sub-triangle
        current_row_data = sub_triangle[-1][:]  # Start with the bottom-most row

        # Iterate upwards from the second to last row down to the top of the sub-triangle
        # Index 'i' in this loop refers to the index within the `sub_triangle` list
        for i in range(len(sub_triangle) - 2, -1, -1):
            # Determine the number of elements in the current row we are processing
            row_width = len(sub_triangle[i])

            # Create a new list for the current row's results
            # The length of the previous (lower) row was row_width + 1
            prev_row_data = current_row_data

            new_row_results = []

            for j in range(row_width):
                # Value at current position (j) in current row 'i'
                current_val = sub_triangle[i][j]

                # The two possible next steps in the row below (row i+1) are at indices j and j+1
                next_val_left = prev_row_data[j]
                next_val_right = prev_row_data[j + 1]

                # Calculate the maximum path sum starting from this node
                # It is the current node value + the maximum of the two possible paths below
                path_sum_through_j = current_val + max(next_val_left, next_val_right)

                new_row_results.append(path_sum_through_j)

            # Update current_row_data for the next iteration of the outer loop
            current_row_data = new_row_results

        # After processing all rows upwards, the first element of current_row_data
        # contains the maximum path sum starting from the very top of our sub-triangle
        return current_row_data[0]

    # Step 3: Call the helper function with validated and sliced inputs
    # We pass the original triangle and the specific row range to the helper
    result = solve_subtriangle(triangle, row_start, row_end)

    return result