def closest_num(n: int) -> int:
    """
    Find the closest smaller number than n.

    This function returns the integer immediately preceding n (i.e., n - 1).
    It assumes n is an integer. If n is not an integer, it raises a TypeError.

    Edge cases:
    - n = 0 -> returns -1
    - n = negative number -> returns the next lower integer
    - n is very large -> returns n - 1 (subject to Python's arbitrary precision integers)

    No validation for integer range is performed beyond type checking, as Python
    handles arbitrary-precision integers.

    Examples:
    >>> closest_num(11)
    10
    >>> closest_num(7)
    6
    >>> closest_num(12)
    11
    """

    # Validate the input type
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Handle the logic: the closest smaller integer is simply n minus one.
    # We compute this using an intermediate variable for clarity.
    candidate = n - 1

    # The problem defines "closest smaller number" in a context where the domain
    # of numbers is implied to be integers. There is no restriction mentioned
    # that prevents the result from being negative or zero.
    # Therefore, for any integer n, the closest smaller integer is n - 1.

    return candidate