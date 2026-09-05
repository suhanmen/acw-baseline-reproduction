def min_flip_to_make_string_alternate(s: str) -> int:
    """
    Finds the minimum number of flips required to make a binary string 
    an alternating sequence (e.g., "0101..." or "1010...").
    """
    n = len(s)
    # Case 1: Target pattern is 010101...
    # Case 2: Target pattern is 101010...
    flips_case1 = 0
    flips_case2 = 0

    for i in range(n):
        # Expected characters for Case 1 (starts with 0)
        expected1 = '0' if i % 2 == 0 else '1'
        # Expected characters for Case 2 (starts with 1)
        expected2 = '1' if i % 2 == 0 else '0'

        if s[i] != expected1:
            flips_case1 += 1
        if s[i] != expected2:
            flips_case2 += 1

    return min(flips_case1, flips_case2)