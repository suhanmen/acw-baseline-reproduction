def eulerian_num(n, m):
    """
    Compute the Eulerian number A(n, m), which counts the number of permutations
    of the set {1, 2, ..., n} with exactly m ascents.

    Uses the recurrence relation:
    A(n, m) = (m + 1) * A(n-1, m) - (n - m) * A(n-1, m - 1)

    Base cases:
    A(0, 0) = 1
    A(n, 0) = 2^(n-1) for n > 0? No, we use recurrence from A(1,0)=1, A(1,1)=0.
    Actually, standard base: A(1, 0) = 1, and A(n, m) = 0 if m < 0 or m >= n.

    We'll build iteratively for clarity and efficiency.
    """
    if n == 0:
        return 1 if m == 0 else 0
    if m < 0 or m >= n:
        return 0

    # dp[k] will store A(current_n, k)
    # Start with n = 1
    dp = [0] * 2  # for n=1, m can be 0 only (since m < n)
    dp[0] = 1

    for i in range(2, n + 1):
        new_dp = [0] * (i)  # for current i, m ranges from 0 to i-1
        for j in range(i):  # j is the current m (which is m for A(i, j))
            # A(i, j) = (j + 1) * A(i-1, j) - (i - j) * A(i-1, j-1)
            term1 = (j + 1) * dp[j] if j < len(dp) else 0
            term2 = (i - j) * dp[j - 1] if j - 1 >= 0 else 0
            new_dp[j] = term1 - term2
        dp = new_dp

    return dp[m]