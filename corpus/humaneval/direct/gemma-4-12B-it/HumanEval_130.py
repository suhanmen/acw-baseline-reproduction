def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n < 0:
        return []

    # We need to find values up to n.
    # The definition of tri(n) for odd n depends on tri(n+1).
    # Let's evaluate the rules:
    # tri(0) is not explicitly defined in the text, but the example tri(3) = [1, 3, 2, 8]
    # suggests tri(0) = 1, tri(1) = 3, tri(2) = 2, tri(3) = 8.

    # Based on the examples provided:
    # tri(0) = 1
    # tri(1) = 3 (given: tri(1) = 3)
    # tri(2) = 1 + 2/2 = 2 (given: tri(n) = 1 + n/2 if n is even)
    # tri(4) = 1 + 4/2 = 3 (given: tri(n) = 1 + n/2 if n is even)
    # tri(3) = tri(2) + tri(1) + tri(4) = 2 + 3 + 3 = 8 (given: tri(n) = tri(n-1) + tri(n-2) + tri(n+1) if n is odd)

    # Since tri(n) for odd n depends on tri(n+1), and tri(n+1) for even n+1 is 1 + (n+1)/2,
    # we can compute any tri(k) directly.

    def get_val(k):
        if k == 0:
            return 1
        if k % 2 == 0:
            return 1 + (k // 2)
        else:
            # tri(k) = tri(k-1) + tri(k-2) + tri(k+1)
            # Since k is odd, k-1 and k+1 are even.
            # tri(k-1) = 1 + (k-1)/2
            # tri(k-2) = ? Wait, if k-2 is odd, it depends on k-1 and k-3...
            # However, for small n, the example tri(3) = tri(2) + tri(1) + tri(4)
            # shows that tri(odd) depends on tri(even) values.
            # Let's look at the recurrence again.
            # tri(1) = 3
            # tri(3) = tri(2) + tri(1) + tri(4)
            # tri(5) = tri(4) + tri(3) + tri(6)
            # In general, for odd k: tri(k) = tri(k-1) + tri(k-2) + tri(k+1)
            # If we assume tri(k-2) is also calculated via this rule, we get a system of equations.
            # But the example tri(3) uses tri(1) as a base value.
            # Let's re-examine: tri(1) is given as 3.
            # tri(3) = tri(2) + tri(1) + tri(4)
            # tri(5) = tri(4) + tri(3) + tri(6)
            # This means for odd k > 1, we can compute it if we know tri(k-1), tri(k-2), tri(k+1).
            # But tri(k-2) for k=3 is tri(1), which is 3.
            # For k=5, tri(k-2) is tri(3), which we just calculated.
            # So we can compute them iteratively.
            pass

    res = [0] * (n + 1)
    if n >= 0: res[0] = 1
    if n >= 1: res[1] = 3

    # Pre-calculate even indices up to n+1 because odd indices depend on them
    # Actually, let's just compute them one by one.
    # Because tri(k) for odd k depends on tri(k+1), we need tri(k+1) which is even.
    # Any tri(even) is 1 + k/2.

    def calculate_tri(k):
        if k == 0: return 1
        if k % 2 == 0: return 1 + (k // 2)
        if k == 1: return 3
        # For odd k > 1:
        # tri(k) = tri(k-1) + tri(k-2) + tri(k+1)
        # tri(k-1) is even: 1 + (k-1)/2
        # tri(k+1) is even: 1 + (k+1)/2
        # tri(k-2) is odd: calculated previously
        return calculate_tri(k-1) + calculate_tri(k-2) + calculate_tri(k+1)

    # Since calculate_tri(k) for odd k depends on k-2, we can fill the list linearly.
    # For odd k, tri(k) = (1 + (k-1)/2) + tri(k-2) + (1 + (k+1)/2)
    # tri(k) = 1 + (k-1)/2 + tri(k-2) + 1 + (k+1)/2
    # tri(k) = 2 + (k-1+k+1)/2 + tri(k-2)
    # tri(k) = 2 + k + tri(k-2)

    # Let's check tri(3) with this: tri(3) = 2 + 3 + tri(1) = 5 + 3 = 8. Correct!

    for i in range(n + 1):
        if i == 0:
            res[i] = 1
        elif i == 1:
            res[i] = 3
        elif i % 2 == 0:
            res[i] = 1 + (i // 2)
        else:
            # tri(i) = 2 + i + tri(i-2)
            res[i] = 2 + i + res[i-2]

    return res