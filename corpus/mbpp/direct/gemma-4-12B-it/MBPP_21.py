def multiples_of_num(m, n):
    """
    Finds m number of multiples of n.
    Wait, looking at the assertions:
    multiples_of_num(4, 3) -> [3, 6, 9, 12] (4 multiples of 3)
    multiples_of_num(2, 5) -> [5, 10] (2 multiples of 5)
    multiples_of_num(9, 2) -> [2, 4, 6, 8, 10, 12, 14, 16, 18] (9 multiples of 2)

    Actually, the pattern shows:
    m = count of multiples
    n = the base number to find multiples of.
    """
    return [i * n for i in range(1, m + 1)]