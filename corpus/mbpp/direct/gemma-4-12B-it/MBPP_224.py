def count_Set_Bits(n: int) -> int:
    """
    Counts the number of set bits (1s) in the binary representation of an integer.
    Uses Brian Kernighan's algorithm for O(k) complexity where k is the number of set bits.
    """
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

if __name__ == "__main__":
    assert count_Set_Bits(2) == 1
    assert count_Set_Bits(4) == 1
    assert count_Set_Bits(6) == 2