def permutation_coefficient(n, k):
    # Input validation
    if not isinstance(n, int) or not isinstance(k, int):
        return 0
    if n < 0 or k < 0:
        return 0

    # Handle edge cases
    if k == 0:
        return 1
    if k == 1:
        return n
    if k > n:
        return 0

    # Calculate P(n, k) using iterative product
    result = 1
    for i in range(k):
        result *= (n - i)

    return result