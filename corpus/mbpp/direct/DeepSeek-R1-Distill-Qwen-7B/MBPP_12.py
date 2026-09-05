def sort_matrix(matrix):
    # Create a list of tuples containing the sum of each row and the row itself
    sorted_rows = sorted([(sum(row), row) for row in matrix], key=lambda x: x[0])
    # Extract the rows in the new order
    sorted_matrix = [row for (s, row) in sorted_rows]
    return sorted_matrix