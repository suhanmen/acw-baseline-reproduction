def ncr_modp(n, r, p):
    """
    Computes (nCr) % p using Lucas's Theorem and Modular Inverse.
    Handles cases where p is prime. 
    Note: For the provided assertions, p is prime (13, 43, 18 is not prime, 
    but 18 is handled by general small nCr if we don't assume Lucas).
    Since 18 is not prime, a standard Pascal's triangle approach is safest 
    for small n, or a prime factorization approach for larger n.
    Given the assertions, n is small.
    """
    if r < 0 or r > n:
        return 0
    if r == 0 or r == n:
        return 1 % p
    if r > n // 2:
        r = n - r

    # Using dynamic programming (Pascal's Triangle) to handle non-prime p
    # because the assertion ncr_modp(17,9,18) implies p might not be prime.
    dp = [[0] * (r + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(min(i, r) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1 % p
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % p
    return dp[n][r]