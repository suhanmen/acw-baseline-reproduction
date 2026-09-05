def even_binomial_Coeff_Sum(n):
    # Step 1: Validate the input
    if not isinstance(n, int) or n < 0:
        return 0

    # Step 2: Handle the case when n is 0
    if n == 0:
        return 1

    # Step 3: Compute the sum using the formula 2^(n-1)
    return 2 ** (n - 1)