def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 1:
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return 1

    # Calculate the sum using the arithmetic series formula
    total = n * (n + 1) // 2
    return total