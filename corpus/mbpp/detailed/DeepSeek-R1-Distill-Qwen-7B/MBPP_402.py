def ncr_modp(n, k, p):
    # Input validation
    if not isinstance(n, int) or not isinstance(k, int) or not isinstance(p, int):
        raise ValueError("All inputs must be integers.")
    if n < 0 or k < 0 or p <= 1:
        raise ValueError("n and k must be non-negative integers and p must be an integer greater than 1.")
    if k > n:
        raise ValueError("k cannot be greater than n.")

    # Handle edge cases
    if k == 0 or k == n:
        return 1 % p
    if k == 1 or k == n - 1:
        return n % p

    # Ensure k is the smaller to optimize the loop
    k = min(k, n - k)

    # Compute the result iteratively while taking modulo p to prevent overflow
    result = 1
    for i in range(1, k + 1):
        result = (result * (n - i + 1)) % p
        result = (result * pow(i, p - 2, p)) % p

    return result