def is_octagonal(n):
    """
    Calculates the nth octagonal number.
    The formula for the nth octagonal number is: n * (3 * n - 2)
    """
    return n * (3 * n - 2)

if __name__ == "__main__":
    assert is_octagonal(5) == 65
    assert is_octagonal(10) == 280
    assert is_octagonal(15) == 645