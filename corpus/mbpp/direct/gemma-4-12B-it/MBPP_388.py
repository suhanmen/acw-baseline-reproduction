def highest_Power_of_2(n):
    """
    Finds the highest power of 2 that is less than or equal to n.
    """
    if n < 1:
        return 0
    # Use bit manipulation: find the position of the most significant bit.
    # For n > 0, (n.bit_length() - 1) gives the index of the MSB.
    return 1 << (n.bit_length() - 1)

if __name__ == "__main__":
    assert highest_Power_of_2(10) == 8
    assert highest_Power_of_2(19) == 16
    assert highest_Power_of_2(32) == 32