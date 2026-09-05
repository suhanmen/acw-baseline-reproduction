def specified_element(matrix, index):
    """
    Extracts the element at the specified index from each sub-list
    in a two-dimensional list.
    """
    return [row[index] for row in matrix]