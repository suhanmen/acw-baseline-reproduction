def min_of_three(a: int, b: int, c: int) -> int:
    """
    Finds and returns the minimum of three numbers.
    """
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

if __name__ == "__main__":
    assert min_of_three(10, 20, 0) == 0
    assert min_of_three(19, 15, 18) == 15
    assert min_of_three(-10, -20, -30) == -30