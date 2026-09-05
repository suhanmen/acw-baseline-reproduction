def next_Power_Of_2(n):
    """
    Returns the smallest power of 2 greater than or equal to n.
    """
    if n <= 0:
        return 1

    # If n is already a power of 2, return n
    # (n & (n - 1)) == 0 checks if n is a power of 2
    if (n & (n - 1)) == 0:
        return n

    # Find the position of the highest set bit and shift 1 to the next position
    return 1 << n.bit_length()