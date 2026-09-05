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
    # Precompute remainders mod 3 for the array values
    # a[i] = i*i - i + 1 for i from 1 to n
    remainders = []
    for i in range(1, n + 1):
        val = i * i - i + 1
        remainders.append(val % 3)

    # Count occurrences of each remainder (0, 1, 2)
    count = [0, 0, 0]
    for r in remainders:
        count[r] += 1

    total = 0

    # Case 1: All three have remainder 0
    if count[0] >= 3:
        total += count[0] * (count[0] - 1) * (count[0] - 2) // 6

    # Case 2: All three have remainder 1
    if count[1] >= 3:
        total += count[1] * (count[1] - 1) * (count[1] - 2) // 6

    # Case 3: All three have remainder 2
    if count[2] >= 3:
        total += count[2] * (count[2] - 1) * (count[2] - 2) // 6

    # Case 4: One of each (0, 1, 2)
    total += count[0] * count[1] * count[2]

    return total