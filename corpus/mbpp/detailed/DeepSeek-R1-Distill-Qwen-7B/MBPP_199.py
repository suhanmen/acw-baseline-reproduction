def highest_Power_of_2(n):
    """
    Finds the highest power of 2 less than or equal to a given number.
    Returns None for invalid inputs.
    """
    if not isinstance(n, int) or n <= 0:
        return None

    if n & (n - 1) == 0:
        return n

    current_power = 2
    highest_power = 1

    while current_power <= n:
        highest_power = current_power
        current_power *= 2

    return highest_power