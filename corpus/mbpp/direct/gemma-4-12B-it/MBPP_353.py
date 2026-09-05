def remove_column(matrix, col_index):
    """
    Removes a specified column index from a nested list.
    Note: If rows have varying lengths, it only removes the element 
    at that index if it exists in the row.
    """
    result = []
    for row in matrix:
        if 0 <= col_index < len(row):
            # Create a new row excluding the element at col_index
            new_row = row[:col_index] + row[col_index+1:]
            result.append(new_row)
        else:
            # If the index is out of bounds for a specific row,
            # the problem requirements suggest the row remains as is 
            # or behaves like a standard list slice.
            # Based on the provided assertions, all rows in the target 
            # rows contain the index.
            result.append(row)
    return result