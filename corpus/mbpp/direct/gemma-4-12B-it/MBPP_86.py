def centered_hexagonal_number(n: int) -> int:
    """
    Calculates the nth centered hexagonal number.
    The formula for the nth centered hexagonal number is:
    H(n) = 3n(n - 1) + 1
    """
    return 3 * n * (n - 1) + 1