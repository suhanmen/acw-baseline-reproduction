def eulerian_num(n: int, m: int) -> int:
    """
    Computes the Eulerian number A(n, m) using the recursive relation:

    A(n, m) = (m + 1) * A(n - 1, m) - (n - m + 1) * A(n - 1, m - 1)

    with base cases:
    - A(0, 0) = 1
    - A(n, 0) = 0 for n > 0
    - A(n, n) = 0 for n > 0
    - A(n, m) = 0 if m < 0 or m > n

    Parameters:
    n (int): The row number (must be non-negative).
    m (int): The column number (must be between 0 and n inclusive).

    Returns:
    int: The Eulerian number A(n, m).

    Raises:
    ValueError: If inputs are not integers, n is negative, or m is out of bounds.
    TypeError: If inputs are not of integer type.
    """

    # Validate input types
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError(f"Both arguments must be of type 'int'. Got n={type(n).__name__}, m={type(m).__name__}.")

    # Validate n
    if n < 0:
        raise ValueError(f"n must be non-negative. Received n={n}.")

    # Validate m
    if m < 0 or m > n:
        raise ValueError(f"m must be between 0 and n inclusive (0 <= m <= n). Received n={n}, m={m}.")

    # Base case: A(0, 0) = 1
    if n == 0 and m == 0:
        return 1

    # Helper function for recursive calculation
    def _compute_eulerian(current_n: int, current_m: int) -> int:
        # Base case 1: n == 0
        if current_n == 0:
            if current_m == 0:
                return 1
            else:
                return 0

        # Base case 2: m == 0
        if current_m == 0:
            return 0

        # Base case 3: m == current_n
        if current_m == current_n:
            return 0

        # Recursive step
        # A(n, m) = (m + 1) * A(n - 1, m) - (n - m + 1) * A(n - 1, m - 1)
        term1_value = current_m + 1
        term1_result = _compute_eulerian(current_n - 1, current_m)
        product1 = term1_value * term1_result

        term2_value = current_n - current_m + 1
        term2_result = _compute_eulerian(current_n - 1, current_m - 1)
        product2 = term2_value * term2_result

        final_result = product1 - product2
        return final_result

    # Call the helper function with validated inputs
    result = _compute_eulerian(n, m)

    return result