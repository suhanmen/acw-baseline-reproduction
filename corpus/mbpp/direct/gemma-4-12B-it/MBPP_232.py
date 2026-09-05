def larg_nnum(data, n):
    """
    Returns the n largest items from a dataset in descending order.
    """
    return sorted(data, reverse=True)[:n]

if __name__ == "__main__":
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2) == [100, 90]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 5) == [100, 90, 80, 70, 60]
    assert larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 3) == [100, 90, 80]