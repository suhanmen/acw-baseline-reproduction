def ap_sum(a, d, n):
    """
    Calculates the sum of an arithmetic progression.

    Args:
        a: The first term of the progression.
        d: The common difference.
        n: The number of terms.

    Returns:
        The sum of the arithmetic progression.
    """
    # Formula for the sum of the first n terms of an AP:
    # S_n = (n / 2) * [2a + (n - 1)d]
    return (n * (2 * a + (n - 1) * d)) // 2