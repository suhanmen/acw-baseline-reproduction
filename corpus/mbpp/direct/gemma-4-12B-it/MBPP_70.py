def get_equal(tuples_list, length):
    """
    Checks if all tuples in the given list have the specified length.

    Args:
        tuples_list (list): A list of tuples.
        length (int): The expected length of each tuple.

    Returns:
        str: A message indicating whether all tuples have the same length.
    """
    for t in tuples_list:
        if len(t) != length:
            return 'All tuples do not have same length'
    return 'All tuples have same length'

if __name__ == "__main__":
    assert get_equal([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
    assert get_equal([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
    assert get_equal([(1, 2), (3, 4)], 2) == 'All tuples have same length'