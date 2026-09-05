def set_Bit_Number(n: int) -> int:
    """
    Finds the most significant bit number (the largest power of 2) 
    that is also a set bit in the given integer n.
    """
    if n <= 0:
        return 0

    # Find the highest power of 2 less than or equal to n
    # bit_length() returns the number of bits required to represent n
    # 2^(bit_length - 1) gives the value of the most significant bit
    return 1 << (n.bit_length() - 1)

if __name__ == "__main__":
    assert set_Bit_Number(6) == 4
    assert set_Bit_Number(10) == 8
    assert set_Bit_Number(18) == 16