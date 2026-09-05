def count_unset_bits(n: int) -> int:
    """
    Count the number of unset (0) bits in the binary representation of n.
    We consider bits up to the most significant bit of n (ignoring leading zeros).
    """
    if n == 0:
        return 0

    count = 0
    while n:
        if n & 1 == 0:
            count += 1
        n >>= 1
    return count