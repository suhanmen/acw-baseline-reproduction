def highest_Power_of_2(n):
    """
    Finds the highest power of 2 less than or equal to a given number n.
    """
    if n < 1:
        return None

    # Using bit manipulation:
    # Find the position of the most significant bit.
    # 2 ** (number of bits - 1) gives the highest power of 2.
    return 1 << (n.bit_length() - 1)

if __name__ == "__main__":
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32