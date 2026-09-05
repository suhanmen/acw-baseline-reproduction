def diff_consecutivenums(lst):
    """
    Finds the difference between two consecutive numbers in a given list.

    Args:
        lst (list): A list of numbers.

    Returns:
        list: A list of differences between consecutive elements.
    """
    if len(lst) < 2:
        return []

    differences = []
    for i in range(len(lst) - 1):
        differences.append(lst[i+1] - lst[i])
    return differences

if __name__ == "__main__":
    assert diff_consecutivenums([1, 1, 3, 4, 4, 5, 6, 7]) == [0, 2, 1, 0, 1, 1, 1]
    assert diff_consecutivenums([4, 5, 8, 9, 6, 10]) == [1, 3, 1, -3, 4]
    assert diff_consecutivenums([0, 1, 2, 3, 4, 4, 4, 4, 5, 7]) == [1, 1, 1, 1, 0, 0, 0, 1, 2]