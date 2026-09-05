def octagonal_number(n):
    # Validate input
    if not isinstance(n, int) or n < 0:
        return None

    # Calculate the nth octagonal number
    n_squared = n ** 2
    term1 = 3 * n_squared
    term2 = 2 * n
    result = term1 - term2

    return result