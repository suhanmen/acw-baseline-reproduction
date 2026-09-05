def remove_column(matrix, col_index):
    return [row[:col_index] + row[col_index + 1:] for row in matrix]