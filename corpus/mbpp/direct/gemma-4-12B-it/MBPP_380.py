def multi_list(rows, cols):
    """
    Generates a two-dimensional array where each element at position (i, j)
    is the product of the row index i and the column index j.
    """
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * j)
        result.append(row)
    return result