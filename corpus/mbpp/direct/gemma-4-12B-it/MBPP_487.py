def sort_tuple(tuples_list):
    """
    Sorts a list of tuples in increasing order based on the last element of each tuple.

    Args:
        tuples_list (list of tuples): A list containing tuples of any size.

    Returns:
        list of tuples: The sorted list.
    """
    return sorted(tuples_list, key=lambda x: x[-1])

if __name__ == "__main__":
    assert sort_tuple([(1, 3), (3, 2), (2, 1)]) == [(2, 1), (3, 2), (1, 3)]
    assert sort_tuple([(2, 4), (3, 3), (1, 1)]) == [(1, 1), (3, 3), (2, 4)]
    assert sort_tuple([(3, 9), (6, 7), (4, 3)]) == [(4, 3), (6, 7), (3, 9)]