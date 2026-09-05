import collections

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
    # Validation: Check if n is a positive integer as per requirements.
    if not isinstance(n, int):
        raise ValueError("Input n must be an integer.")
    if n < 1:
        # The problem specifies n is a positive integer, but we handle 
        # non-positive values defensively.
        return 0

    # A triple (a[i], a[j], a[k]) satisfies (a[i] + a[j] + a[k]) % 3 == 0.
    # This is a combinatorics problem based on the remainders of the elements when divided by 3.
    # We count how many elements in the array have remainders 0, 1, and 2.

    # Initialize counts for remainders 0, 1, and 2
    remainder_counts = {0: 0, 1: 0, 2: 0}

    # Step 1: Generate the values and count remainders.
    # We use a loop to generate a[i] = i^2 - i + 1 for 1 <= i <= n.
    # To save memory, we don't need to store the entire list 'a',
    # only the count of each remainder modulo 3.
    for i in range(1, n + 1):
        val = (i * i) - i + 1
        rem = val % 3
        remainder_counts[rem] += 1

    # Step 2: Calculate combinations that sum to a multiple of 3.
    # Let c0, c1, c2 be the number of elements with remainder 0, 1, and 2.
    # The possible combinations of remainders (r1, r2, r3) such that 
    # (r1 + r2 + r3) % 3 == 0 are:
    # 1. (0, 0, 0) -> All three elements have remainder 0.
    # 2. (1, 1, 1) -> All three elements have remainder 1.
    # 3. (2, 2, 2) -> All three elements have remainder 2.
    # 4. (0, 1, 2) -> One element of each remainder.

    c0 = remainder_counts[0]
    c1 = remainder_counts[1]
    c2 = remainder_counts[2]

    total_triples = 0

    # Case 1: Three elements with remainder 0.
    # Number of ways is combination(c0, 3) = c0 * (c0-1) * (c0-2) / 6
    if c0 >= 3:
        ways_000 = (c0 * (c0 - 1) * (c0 - 2)) // 6
        total_triples += ways_000

    # Case 2: Three elements with remainder 1.
    # Number of ways is combination(c1, 3) = c1 * (c1-1) * (c1-2) / 6
    if c1 >= 3:
        ways_111 = (c1 * (c1 - 1) * (c1 - 2)) // 6
        total_triples += ways_111

    # Case 3: Three elements with remainder 2.
    # Number of ways is combination(c2, 3) = c2 * (c2-1) * (c2-2) / 6
    if c2 >= 3:
        ways_222 = (c2 * (c2 - 1) * (c2 - 2)) // 6
        total_triples += ways_222

    # Case 4: One element of remainder 0, one of 1, and one of 2.
    # Number of ways is c0 * c1 * c2
    if c0 >= 1 and c1 >= 1 and c2 >= 1:
        ways_012 = c0 * c1 * c2
        total_triples += ways_012

    return total_triples