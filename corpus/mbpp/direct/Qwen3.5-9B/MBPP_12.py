def sort_matrix(matrix):
    return sorted(matrix, key=lambda row: sum(row))