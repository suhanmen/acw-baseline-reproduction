def eulerian_num(n: int, m: int) -> int:
    """
    Calculates the Eulerian number A(n, m), which counts the number of
    permutations of 1 to n that have exactly m descents (or ascents).

    The recurrence relation is:
    A(n, m) = (m + 1) * A(n-1, m) + (n - m) * A(n-1, m-1)
    with base cases:
    A(n, 0) = 1
    A(n, n-1) = 1
    """
    if m < 0 or m >= n:
        return 0
    if m == 0 or m == n - 1:
        return 1

    # Use dynamic programming to build a table of Eulerian numbers
    # dp[i][j] will store A(i, j)
    dp = [[0 for _ in range(n)] for _ in range(n + 1)]

    # Base cases for n=1
    dp[1][0] = 1

    for i in range(2, n + 1):
        for j in range(i):
            # Formula: A(n, m) = (m + 1) * A(n-1, m) + (n - m) * A(n-1, m-1)
            # Note: In our 0-indexed j represents 'm'
            term1 = (j + 1) * dp[i-1][j]
            term2 = (i - j) * (dp[i-1][j-1] if j > 0 else 0)
            dp[i][j] = term1 + term2

    return dp[n][m]