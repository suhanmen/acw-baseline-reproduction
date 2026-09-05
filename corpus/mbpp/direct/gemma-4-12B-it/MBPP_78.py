def count_With_Odd_SetBits(n: int) -> int:
    """
    Counts the number of integers from 0 to n (inclusive) that have 
    an odd number of set bits in their binary representation.
    """
    count = 0
    for i in range(n + 1):
        # bin(i).count('1') returns the number of set bits
        if bin(i).count('1') % 2 != 0:
            count += 1
    return count