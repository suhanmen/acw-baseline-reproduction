def closest_num(n):
    """
    Returns the closest smaller number than n.
    In the context of integers, this is n - 1.
    """
    return n - 1

if __name__ == "__main__":
    assert closest_num(11) == 10
    assert closest_num(7) == 6
    assert closest_num(12) == 11