def remove_column(data: list, column_index: int) -> list:
    """
    Removes a specified column from a given nested list (list of lists).

    This function performs rigorous validation and defensive programming:
    1. Validates that 'data' is a list and 'column_index' is an integer.
    2. Validates that 'column_index' is within the bounds of a valid row length.
    3. Handles rows of varying lengths by using a try-except block to skip or handle
       rows that do not contain the specified column (though the problem implies
       a rectangular matrix, production code must handle degenerate cases).
    4. Returns a new list of lists with the specified column removed.

    Args:
        data (list): A list of lists representing rows.
        column_index (int): The zero-based index of the column to remove.

    Returns:
        list: A new list of lists with the specified column removed.

    Raises:
        TypeError: If 'data' is not a list or 'column_index' is not an int/bool (bool is subclass of int).
        ValueError: If 'column_index' is out of bounds for the data structure.
    """

    # Step 1: Validate the 'data' argument
    if not isinstance(data, list):
        raise TypeError("The 'data' argument must be a list.")

    # Step 2: Validate the 'column_index' argument
    # We check for int explicitly. In Python, bool is a subclass of int, so True/False would pass int check.
    # Usually, for column indices, we want a true integer.
    if not isinstance(column_index, int) or isinstance(column_index, bool):
        raise TypeError("The 'column_index' argument must be an integer.")

    # Step 3: Handle the empty data case
    if len(data) == 0:
        # If there are no rows, we return an empty list immediately.
        # No column index matters for an empty matrix.
        return []

    # Step 4: Validate the column index against the first row
    # We assume the data is "rectangular" enough that the first row defines the expected width.
    # If the first row is empty, any column index > 0 is invalid.
    first_row = data[0]

    # Get the length of the first row.
    first_row_length = len(first_row)

    # Check if the column_index is a valid index for the first row.
    # Valid indices are 0 <= index < length.
    if column_index < 0 or column_index >= first_row_length:
        raise ValueError(
            f"The column_index '{column_index}' is out of bounds. "
            f"The first row has length '{first_row_length}'. "
            f"Valid indices are 0 to {first_row_length - 1}."
        )

    # Step 5: Initialize the result list
    result_rows = []

    # Step 6: Iterate through each row in the input data
    for current_row in data:
        # Validate that current_row is actually a list before indexing
        if not isinstance(current_row, list):
            raise TypeError(f"Expected a list of lists, but encountered a non-list row: {current_row}")

        # Create a new list for the current row by extending the previous list of new rows?
        # No, better to build the new row and then append it.

        # Create a list containing elements of the current row
        new_row_list = []

        # Iterate through the indices of the current row
        current_row_index = 0
        for value in current_row:
            # Check if this is the index of the column to be removed
            is_target_column = (current_row_index == column_index)

            if is_target_column:
                # Skip this value
                pass
            else:
                # Append this value to the new row
                new_row_list.append(value)

            # Increment the index for the next iteration
            current_row_index += 1

        # Append the constructed new row to the result list
        result_rows.append(new_row_list)

    # Step 7: Return the final result
    return result_rows