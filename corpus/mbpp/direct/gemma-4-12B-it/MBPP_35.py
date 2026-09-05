def find_rect_num(n: int) -> int:
    """
    Finds the n-th rectangular number.
    A rectangular number (or pronic number) is a number that is the product of two 
    consecutive integers. The n-th rectangular number is defined as n * (n + 1).
    """
    return n * (n + 1)

if __name__ == "__main__":
    assert find_rect_num(4) == 20
    assert find_rect_num(5) == 30
    assert find_rect_num(6) == 42