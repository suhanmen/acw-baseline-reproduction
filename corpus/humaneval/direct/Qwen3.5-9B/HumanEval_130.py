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
    if n == 0:
        return [1]

    # Initialize the sequence with known values for small n
    # We need to compute up to index n
    # Base case: tri(0) is not explicitly defined but from example tri(3) = [1, 3, 2, 8]
    # Index 0 -> 1, Index 1 -> 3, Index 2 -> 2, Index 3 -> 8
    # So tri(0) = 1, tri(1) = 3
    sequence = [1, 3]

    # We need to fill up to index n
    # If n is 1, we just return [1, 3]
    if n == 1:
        return sequence

    # We need to handle the recursive definition carefully.
    # tri(n) depends on tri(n+1) for odd n, which creates a circular dependency if we don't plan ahead.
    # However, the problem statement gives examples that suggest a specific pattern or termination.
    # Let's re-examine:
    # tri(1) = 3 (given)
    # tri(2) = 1 + 2/2 = 2
    # tri(3) = tri(2) + tri(1) + tri(4). We know tri(3)=8.
    # 8 = 2 + 3 + tri(4) => 8 = 5 + tri(4) => tri(4) = 3.
    # Check tri(4) with even formula: 1 + 4/2 = 3. Matches.
    #
    # Strategy:
    # 1. Precompute all even numbers up to n using the even formula.
    # 2. For odd numbers, we might need values of higher indices, but those higher indices
    #    will likely be even (or stop at a known even base).
    # Actually, the recurrence for odd n uses n+1. If n is odd, n+1 is even.
    # So tri(n) (odd) = tri(n-1) + tri(n-2) + tri(n+1)
    # tri(n-1) is even. tri(n-2) is odd. tri(n+1) is even.
    # This means to compute an odd number, we need a higher odd number (n-2) and two evens.
    # This looks like it could go on indefinitely if we try to compute from 1 upwards blindly.
    # But notice the pattern:
    # tri(3) depends on tri(4). tri(4) is even, so it's fixed.
    # tri(5) = tri(4) + tri(3) + tri(6). tri(6) is even.
    # So if we have the sequence up to some point, and we know even numbers are deterministic,
    # we can potentially solve for odd numbers if we view the relation as:
    # tri(n+1) = tri(n) + tri(n-1) - tri(n) ??? No.
    # tri(n) = tri(n-1) + tri(n-2) + tri(n+1)  => tri(n+1) = tri(n) - tri(n-1) - tri(n-2)
    # Wait, the problem says "tri(n) = ... + tri(n+1)".
    # This defines tri(n) using tri(n+1). This is a backward recurrence for odd numbers.
    # However, in the example: tri(3) = 8.
    # tri(3) = tri(2) + tri(1) + tri(4) -> 8 = 2 + 3 + 3.
    # It seems the sequence is fixed by the even terms acting as "anchors".
    # Since we need the first n+1 numbers (indices 0 to n), and n can be up to any integer.
    # But wait, if n is odd, say n=3, we need tri(3). tri(3) depends on tri(4).
    # Do we need to calculate beyond n? Yes, to compute tri(n) for odd n, we need tri(n+1).
    # But tri(n+1) is even, so it's directly computable: 1 + (n+1)/2.
    # What about tri(n-2)? If n=3, n-2=1 (odd). We need tri(1).
    # tri(1) is given as 3.
    # What about tri(5)? tri(5) = tri(4) + tri(3) + tri(6).
    # tri(4) is even (computable). tri(6) is even (computable). tri(3) we just computed.
    # So the strategy:
    # 1. Identify the maximum index we might need. If n is odd, we need n+1. If n is even, we need n.
    #    Actually, to compute odd k, we need k+1. So max index needed is n if n even, n+1 if n odd.
    #    However, looking at the dependency for odd k: tri(k) = tri(k-1) + tri(k-2) + tri(k+1).
    #    tri(k+1) is even -> known.
    #    tri(k-1) is even -> known.
    #    tri(k-2) is odd -> previously computed (since k-2 < k).
    #    So we can compute odd numbers in increasing order if we have all evens.
    #    Evens are simple formulas.
    #    Odds depend on previous odd (k-2) and current evens.
    #
    #    Let's verify:
    #    tri(1) = 3 (Base)
    #    tri(3) = tri(2) + tri(1) + tri(4)
    #            = (1+2/2) + 3 + (1+4/2) = 2 + 3 + 3 = 8. Correct.
    #    tri(5) = tri(4) + tri(3) + tri(6)
    #            = (1+4/2) + 8 + (1+6/2) = 3 + 8 + 4 = 15.
    #    tri(7) = tri(6) + tri(5) + tri(8)
    #            = 4 + 15 + (1+8/2) = 4 + 15 + 5 = 24.
    #
    #    Algorithm:
    #    Target: fill sequence[0]...sequence[n].
    #    If n is odd, we might need sequence[n+1] to calculate sequence[n]?
    #    Wait, the formula is: tri(k) = tri(k-1) + tri(k-2) + tri(k+1).
    #    So to get tri(k), we need tri(k+1).
    #    This means we must know the value at k+1 to get k.
    #    But if we iterate k from 1 to n, when we are at k (odd), we need k+1.
    #    If k=n (and n is odd), we need n+1.
    #    So we should compute up to max(n, n+1 if n is odd) = n+1.
    #    Let limit = n if n%2==0 else n+1.
    #    We compute all evens up to limit.
    #    We set tri(1)=3.
    #    Then for k from 3 to limit step 2 (odd numbers):
    #       tri[k] = tri[k-1] + tri[k-2] + tri[k+1]
    #    But wait, if we compute sequentially, when we are at k, k+1 might not be computed yet?
    #    No, evens are computed on the fly or precomputed.
    #    Specifically, for any k (odd), k+1 is even.
    #    So if we ensure all even indices up to 'limit' are calculated, we can compute any odd k <= limit.
    #
    #    Refined Algorithm:
    #    1. Determine limit = n + (1 if n % 2 != 0 else 0).
    #    2. Create a list `res` of size limit + 1.
    #    3. Set res[0] = 1.
    #    4. Set res[1] = 3.
    #    5. For all even i from 2 to limit: res[i] = 1 + i // 2.
    #    6. For all odd i from 3 to limit (step 2):
    #         res[i] = res[i-1] + res[i-2] + res[i+1]
    #       Note: i-1 is even, i-2 is odd (and < i, so computed), i+1 is even (<= limit, so computed).
    #    7. Return res[0...n].

    limit = n
    if n % 2 != 0:
        limit = n + 1

    res = [0] * (limit + 1)
    res[0] = 1
    if limit >= 1:
        res[1] = 3

    # Fill evens
    for i in range(2, limit + 1, 2):
        res[i] = 1 + i // 2

    # Fill odds
    for i in range(3, limit + 1, 2):
        # Formula: tri(i) = tri(i-1) + tri(i-2) + tri(i+1)
        res[i] = res[i-1] + res[i-2] + res[i+1]

    return res[:n+1]