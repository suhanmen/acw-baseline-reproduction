def big_sum(arr):
    """
    Finds the sum of the largest and smallest value in a given array.

    Args:
        arr (list): A list of integers or floats.

    Returns:
        int/float: The sum of the maximum and minimum values.
    """
    if not arr:
        return 0
    return max(arr) + min(arr)

if __name__ == "__main__":
    assert big_sum([1, 2, 3]) == 4
    assert big_sum([-1, 2, 3, 4]) == 3
    assert big_sum([2, 3, 6]) == 8