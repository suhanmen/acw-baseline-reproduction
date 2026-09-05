def find_length(s: str, length: int) -> int:
    """
    Finds the maximum difference between the number of 0s and 1s 
    in any sub-string of the given binary string.

    The difference is calculated as |count(0) - count(1)|.
    """
    max_diff = 0
    n = len(s)

    # We check every possible substring
    for i in range(n):
        count0 = 0
        count1 = 0
        for j in range(i, n):
            if s[j] == '0':
                count0 += 1
            else:
                count1 += 1

            diff = abs(count0 - count1)
            if diff > max_diff:
                max_diff = diff

    return max_diff