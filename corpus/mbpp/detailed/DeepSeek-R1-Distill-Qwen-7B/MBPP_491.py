def sum_gp(a, n, r):
    """
    Calculate the sum of the first n terms of a geometric progression.

    Parameters:
        a (int): The first term of the geometric progression.
        n (int): The number of terms. Must be a positive integer.
        r (int): The common ratio. Must be a positive integer.

    Returns:
        int: The sum of the first n terms.

    Raises:
        ValueError: If any input is invalid.
    """
    # Handle invalid inputs
    if not isinstance(n, int) or n < 0 or n == 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(r, int) or r <= 0:
        raise ValueError("r must be a positive integer greater than 0")
    if not isinstance(a, int) or a < 0:
        raise ValueError("a must be a non-negative integer")

    # Handle the special case where the ratio is 1
    if r == 1:
        return a * n

    # Calculate the sum using the geometric series formula
    sum_g = a * (r**n - 1) // (r - 1)

    return sum_g