def remove_column(data, column):
    """
    Removes a specified column from each sublist in a nested list.

    Args:
        data: A nested list where each sublist represents a row.
        column: The index of the column to remove.

    Returns:
        A new nested list with the specified column removed from each sublist.

    Raises:
        ValueError: If the input list is empty or if column index is invalid.
    """
    # Validate input
    if not data:
        raise ValueError("The input list is empty.")

    # Determine the number of columns
    num_columns = len(data[0]) if data else 0

    # Validate the column index
    if column < 0 or column >= num_columns:
        # Convert negative index to positive
        column = num_columns + column
        if column < 0 or column >= num_columns:
            raise ValueError("The column index is invalid.")

    # Remove the specified column from each sublist
    result = []
    for sublist in data:
        if not sublist:  # Handle empty sublist
            raise ValueError("Sublist is empty.")
        # Create a new sublist excluding the specified column
        new_sublist = [element for index, element in enumerate(sublist) if index != column]
        result.append(new_sublist)

    return result

# Example usage
print(remove_column([[1, 2, 3], [2, 4, 5], [1, 1, 1]], 0))
# Output: [[2, 3], [4, 5], [1, 1]]

print(remove_column([[1, 2, 3], [-2, 4, -5], [1, -1, 1]], 2))
# Output: [[1, 2], [-2, 4], [1, -1]]

print(remove_column([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]], 0))
# Output: [[3], [7], [3], [15, 17], [7], [11]]