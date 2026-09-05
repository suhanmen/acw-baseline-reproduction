def find_star_num(n: int) -> int:
    """
    Finds the n'th star number.
    A star number is a centered figurate number that represents a centered hexagram.
    The formula for the n'th star number is S_n = 6n(n - 1) + 1.
    """
    return 6 * n * (n - 1) + 1