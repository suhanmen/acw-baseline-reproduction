def check(n: int) -> bool:
    """
    Checks if a given number is one less than twice its reverse.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n == 2 * reverse(n) - 1, False otherwise.
    """
    s = str(n)
    reverse_n = int(s[::-1])
    return n == (2 * reverse_n) - 1

if __name__ == "__main__":
    assert check(70) == False
    assert check(23) == False
    assert check(73) == True