def count_With_Odd_SetBits(n: int) -> int:
    """
    Counts how many integers from 0 to n (inclusive) have an odd number of set bits.
    """
    count = 0
    for i in range(n + 1):
        if bin(i).count('1') % 2 == 1:
            count += 1
    return count