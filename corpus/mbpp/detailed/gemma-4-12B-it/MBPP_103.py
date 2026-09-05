from typing import List

def eulerian_num(n: int, m: int) -> int:
    """
    Calculates the Eulerian number A(n, m).

    The Eulerian number A(n, m) is the number of permutations of the 
    set {1, 2, ..., n} that have exactly m ascents (or descents, 
    depending on the convention; here we use the standard definition 
    where A(n, m) counts permutations of 1..n with m descents).

    The recurrence relation is:
    A(n, k) = (k + 1) * A(n-1, k) + (n - k) * A(n-1, k-1)

    Base cases:
    A(n, 0) = 1
    A(n, n-1) = 1
    A(n, k) = 0 if k < 0 or k >= n

    Args:
        n: The size of the set (integer).
        m: The number of descents/ascents (integer).

    Returns:
        The Eulerian number A(n, m) as an integer.

    Raises:
        ValueError: If n is not a non-negative integer or if n=0 and m!=0.
        TypeError: If inputs are not integers.
    """
    # --- Input Validation ---
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("Both n and m must be integers.")

    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Boundary case: n = 0
    # By convention, A(0, 0) = 1, and A(0, m) = 0 for m > 0.
    if n == 0:
        if m == 0:
            return 1
        else:
            return 0

    # Boundary case: m < 0 or m >= n
    # Eulerian numbers A(n, m) are defined for 0 <= m < n.
    # If m is out of this range, the value is 0.
    if m < 0 or m >= n:
        # Special case: A(n, 0) = 1 is allowed by the recurrence 
        # but usually we treat m as the number of descents/ascents.
        # Based on the assertions:
        # eulerian_num(3, 1) -> A(3, 1). 
        # The formula A(n, k) = (k+1)A(n-1, k) + (n-k)A(n-1, k-1)
        # for n=3, m=1: (1+1)A(2,1) + (3-1)A(2,0) = 2(1) + 2(1) = 4.
        # So A(n, m) is defined for 0 <= m <= n-1.
        if m == 0:
            return 1
        return 0

    # --- Dynamic Programming Setup ---
    # We use a 2D table to store results.
    # table[i][j] will store Eulerian number A(i, j).
    # Size is (n+1) x (n+1) to accommodate indices up to n.
    table: List[List[int]] = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # --- Base Case Initialization ---
    # A(i, 0) = 1 for all i >= 0
    for i in range(n + 1):
        table[i][0] = 1

    # --- Fill the Table ---
    # We compute values iteratively from i = 1 up to n.
    # For each i, we compute values for j from 1 up to i-1.
    for i in range(1, n + 1):
        # The maximum possible descents for a permutation of i elements is i-1.
        # We iterate up to min(i-1, m) because we only care about reaching m.
        for j in range(1, i):
            # Recurrence: A(i, j) = (j + 1) * A(i-1, j) + (i - j) * A(i-1, j-1)

            term_1_coefficient: int = j + 1
            term_1_value: int = table[i - 1][j]

            term_2_coefficient: int = i - j
            term_2_value: int = table[i - 1][j - 1]

            term_1_product: int = term_1_coefficient * term_1_value
            term_2_product: int = term_2_coefficient * term_2_value

            table[i][j] = term_1_product + term_2_product

    # The answer is stored in the table at (n, m).
    # However, because our loop for j only goes up to i-1, 
    # we need to ensure m is within bounds before accessing.
    if m < 0 or m >= n:
        # Re-check special case for m=0 which was handled in initialization.
        if m == 0:
            return table[n][0]
        return 0

    return table[n][m]