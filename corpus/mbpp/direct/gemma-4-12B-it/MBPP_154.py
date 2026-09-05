def specified_element(matrix, index):
    """
    Extracts every element at the specified column index from a 2D list.

    Args:
        matrix (list[list]): A two-dimensional list of elements.
        index (int): The column index to extract.

    Returns:
        list: A list containing the elements at the specified index for each row.
    """
    return [row[index] for row in matrix]

if __name__ == "__main__":
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 0) == [1, 4, 7]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 2) == [3, 6, 9]
    assert specified_element([[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]], 3) == [2, 2, 5]