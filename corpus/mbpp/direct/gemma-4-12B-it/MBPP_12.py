def sort_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Sorts a matrix in ascending order according to the sum of its rows.
    """
    return sorted(matrix, key=lambda row: sum(row))

if __name__ == "__main__":
    assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) == [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
    assert sort_matrix([[1, 2, 3], [-2, 4, -5], [1, -1, 1]]) == [[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
    assert sort_matrix([[5, 8, 9], [6, 4, 3], [2, 1, 4]]) == [[2, 1, 4], [6, 4, 3], [5, 8, 9]]