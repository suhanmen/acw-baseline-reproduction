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
    # The condition a[i] + a[j] + a[k] % 3 == 0 means we need to count
    # how many elements of 'a' have remainders 0, 1, and 2 when divided by 3.

    # Let a[i] = i^2 - i + 1
    # We want to find the remainder of a[i] modulo 3 for i = 1 to n.
    # i % 3 can be 0, 1, or 2.
    # If i % 3 == 0: a[i] % 3 = (0^2 - 0 + 1) % 3 = 1
    # If i % 3 == 1: a[i] % 3 = (1^2 - 1 + 1) % 3 = 1
    # If i % 3 == 2: a[i] % 3 = (2^2 - 2 + 1) % 3 = (4 - 2 + 1) % 3 = 3 % 3 = 0

    count0 = 0
    count1 = 0
    count2 = 0

    for i in range(1, n + 1):
        val = (i * i - i + 1) % 3
        if val == 0:
            count0 += 1
        elif val == 1:
            count1 += 1
        else:
            count2 += 1

    # A triple (x, y, z) sums to a multiple of 3 if:
    # 1. All three have the same remainder mod 3:
    #    (0,0,0), (1,1,1), or (2,2,2)
    # 2. All three have different remainders mod 3:
    #    (0,1,2)

    # Number of ways to pick 3 from count0: C(count0, 3)
    # Number of ways to pick 3 from count1: C(count1, 3)
    # Number of ways to pick 3 from count2: C(count2, 3)
    # Number of ways to pick one from each: count0 * count1 * count2

    def combinations_3(count):
        if count < 3:
            return 0
        return count * (count - 1) * (count - 2) // 6

    total_triples = (combinations_3(count0) + 
                      combinations_3(count1) + 
                      combinations_3(count2) + 
                      (count0 * count1 * count2))

    return total_triples