def swap_numbers(a, b):
    """
    Swaps two numbers and returns them as a tuple.
    """
    a, b = b, a
    return a, b

if __name__ == "__main__":
    assert swap_numbers(10, 20) == (20, 10)
    assert swap_numbers(15, 17) == (17, 15)
    assert swap_numbers(100, 200) == (200, 100)