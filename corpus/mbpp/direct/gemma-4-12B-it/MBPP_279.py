def is_num_decagonal(n: int) -> int:
    """
    Calculates the nth decagonal number.
    The formula for the nth decagonal number is: D_n = 4n^2 - 3n
    """
    return 4 * (n**2) - 3 * n