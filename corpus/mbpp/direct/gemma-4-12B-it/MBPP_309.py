def maximum(a, b):
    """
    Returns the maximum of two numbers.
    """
    if a > b:
        return a
    else:
        return b

if __name__ == "__main__":
    assert maximum(5, 10) == 10
    assert maximum(-1, -2) == -1
    assert maximum(9, 7) == 9