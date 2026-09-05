def sort_matrix(matrix):
    # Input validation: Check if the matrix is empty
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return matrix

    # Check if all rows have the same length
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            return matrix  # Return as is if rows are of unequal length

    # Calculate the sum of each row and pair it with the row
    summed_rows = [(sum(row), row) for row in matrix]

    # Sort the rows based on their sum
    summed_rows.sort(key=lambda x: x[0])

    # Extract the sorted rows
    sorted_matrix = [row for sum_val, row in summed_rows]

    return sorted_matrix