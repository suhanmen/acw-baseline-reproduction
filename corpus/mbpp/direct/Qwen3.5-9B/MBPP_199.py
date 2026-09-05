def highest_Power_of_2(n: int) -> int:
    """
    Returns the highest power of 2 less than or equal to the given number n.
    Assumes n is a positive integer.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    power = 1
    while power * 2 <= n:
        power *= 2
    return power