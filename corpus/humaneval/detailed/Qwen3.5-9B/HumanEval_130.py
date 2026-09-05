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
    # Step 1: Input Validation
    # Ensure the input is an integer.
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received {type(n).__name__}")

    # Ensure the input is non-negative as per the problem description.
    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, received {n}")

    # Step 2: Define the recursive helper function with memoization strategy
    # However, to avoid infinite recursion on the odd case which depends on (n+1),
    # we must realize that the problem definition is slightly circular for a pure
    # recursive call without a stopping mechanism or dynamic programming.
    # The standard approach for such sequence generation where a term depends on a higher index
    # in its definition (tri(n) depends on tri(n+1)) is to compute iteratively or use
    # an infinite cache that resolves forward references once lower bounds are known.
    # BUT, looking closely at the recurrence: tri(n) = tri(n-1) + tri(n-2) + tri(n+1).
    # This rearranges to: tri(n+1) = tri(n) - tri(n-1) - tri(n-2).
    # This implies if we know tri(n), tri(n-1), and tri(n-2), we can find tri(n+1).
    # This allows us to generate the sequence iteratively starting from known base cases.

    # Known base cases from docstring:
    # tri(1) = 3
    # tri(2) = 1 + 2/2 = 2
    # Let's calculate tri(0) based on the pattern if necessary, or handle n=0 specifically.
    # The problem asks for the first n+1 numbers.
    # If n=0, we need index 0.
    # If n=1, we need indices 0, 1.
    # If n=2, we need indices 0, 1, 2.
    # We need to determine tri(0).
    # Let's look at the odd recurrence: tri(1) = tri(0) + tri(-1) + tri(2).
    # We know tri(1)=3, tri(2)=2. We don't have tri(-1).
    # However, the problem statement example: tri(3) = [1, 3, 2, 8].
    # Index 0 is 1. Index 1 is 3. Index 2 is 2. Index 3 is 8.
    # So tri(0) = 1.
    # Let's verify tri(3) using the recurrence:
    # tri(3) = tri(2) + tri(1) + tri(4).
    # 8 = 2 + 3 + tri(4) => tri(4) = 3.
    # Check even formula for tri(4): 1 + 4/2 = 3. Matches.
    # So the sequence starts: tri(0)=1, tri(1)=3, tri(2)=2, tri(3)=8, tri(4)=3, etc.

    # Strategy:
    # 1. Initialize a list with the known start values [1, 3, 2] corresponding to indices 0, 1, 2.
    # 2. If n < 2, we handle slicing carefully.
    # 3. If n >= 2, we need to compute subsequent values.
    #    For an odd index k (k >= 3), tri(k) = tri(k-1) + tri(k-2) + tri(k+1).
    #    This looks like we need tri(k+1). But wait, if we are building forward:
    #    We have tri(k-1) and tri(k-2). We need tri(k).
    #    The formula given is for calculating tri(k) where k is odd.
    #    tri(k) = tri(k-1) + tri(k-2) + tri(k+1).
    #    This requires tri(k+1) to find tri(k). This is a "future" dependency.
    #    
    #    Let's re-read carefully: "tri(n) = tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd."
    #    Usually, sequences are defined to find the next term from previous ones.
    #    If the definition relies on n+1 to define n, we can invert it.
    #    Let m = n + 1. If n is odd, then m is even.
    #    So if we are at an even index m, and we know tri(m-1) and tri(m-2) (where m-1 is odd),
    #    we can find tri(m-1) using the formula for the odd index m-1?
    #    Let's try that path.
    #    We want to find tri(k).
    #    If k is even: tri(k) = 1 + k/2. (Direct calculation)
    #    If k is odd: tri(k) = tri(k-1) + tri(k-2) + tri(k+1).
    #    Rearranging: tri(k+1) = tri(k) - tri(k-1) - tri(k-2).
    #    Here, k is odd, so k+1 is even.
    #    We know how to calculate any even number directly!
    #    So, tri(k+1) = 1 + (k+1)/2.
    #    Therefore, for an odd k: tri(k) = tri(k-1) + tri(k-2) + (1 + (k+1)/2).
    #    
    #    Let's verify with k=3 (odd).
    #    tri(3) = tri(2) + tri(1) + (1 + 4/2) = 2 + 3 + 3 = 8. Correct.
    #    Let's verify with k=1 (odd).
    #    tri(1) = tri(0) + tri(-1) + (1 + 2/2).
    #    We know tri(1)=3. tri(0)=1. 3 = 1 + tri(-1) + 2 => tri(-1) = 0.
    #    But we don't need tri(-1) if we just start computing from n=3 upwards.
    #    The sequence starts at index 0.
    #    Values:
    #    0 (even): 1 + 0/2 = 1. (Matches example start)
    #    1 (odd): Defined as 3. (Base case in docstring).
    #    2 (even): 1 + 2/2 = 2. (Matches example).
    #    3 (odd): 8 (Calculated above).
    #    4 (even): 1 + 4/2 = 3.
    #    5 (odd): tri(4) + tri(3) + tri(6).
    #         tri(6) = 1 + 6/2 = 4.
    #         tri(5) = 3 + 8 + 4 = 15.
    #         Check via recurrence inversion: tri(6) = tri(5) - tri(4) - tri(3) => 4 = 15 - 3 - 8 = 4. Consistent.

    # Step 3: Construct the sequence iteratively
    # We will build a list `result` where result[i] = tri(i).
    # We know:
    #   tri(0) = 1 (derived from example output for n=3 being [1, 3, 2, 8])
    #   tri(1) = 3 (given)
    #   tri(2) = 2 (given)

    result = [0] * (n + 1)

    if n >= 0:
        result[0] = 1
    if n >= 1:
        result[1] = 3
    if n >= 2:
        result[2] = 2

    # Now compute from index 3 up to n
    for i in range(3, n + 1):
        if i % 2 == 0:
            # Even index: direct formula
            # tri(i) = 1 + i / 2
            val_even = 1 + (i // 2)
            result[i] = val_even
        else:
            # Odd index: tri(i) = tri(i-1) + tri(i-2) + tri(i+1)
            # Since i+1 is even, we can calculate tri(i+1) directly.
            # tri(i+1) = 1 + (i+1)/2
            next_val = 1 + ((i + 1) // 2)

            # Calculate current term
            prev_val = result[i - 1]
            prev_prev_val = result[i - 2]

            # tri(i) = prev + prev_prev + next
            current_val = prev_val + prev_prev_val + next_val
            result[i] = current_val

    return result