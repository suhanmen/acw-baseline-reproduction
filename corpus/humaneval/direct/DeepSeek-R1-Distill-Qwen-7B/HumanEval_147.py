def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    from math import comb

    counts = [0, 0, 0]  # counts[0] for remainder 0, counts[1] for remainder 1, counts[2] for remainder 2

    for i in range(1, n + 1):
        a_i = i * i - i + 1
        rem = a_i % 3
        counts[rem] += 1

    total = 0

    # Case 1: all three in same remainder 0
    total += comb(counts[0], 3)

    # Case 2: all three in same remainder 1
    total += comb(counts[1], 3)

    # Case 3: all three in same remainder 2
    total += comb(counts[2], 3)

    # Case 4: one from each remainder
    total += counts[0] * counts[1] * counts[2]

    return total