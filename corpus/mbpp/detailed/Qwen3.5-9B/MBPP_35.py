def find_rect_num(n: int) -> int:
    """
    Calculate the n-th rectangular number.

    A rectangular number (also known as a oblong number or pronic number) 
    represents the number of dots in a rectangular grid with sides of length n 
    and n-1. The formula is R(n) = n * (n - 1).

    Note: The problem examples suggest the input n represents the larger side 
    of the rectangle, so for n=4, we get 4 * 3 = 12. However, the provided 
    assertions expect:
    find_rect_num(4) == 20 (which is 5 * 4)
    find_rect_num(5) == 30 (which is 6 * 5)
    find_rect_num(6) == 42 (which is 7 * 6)

    Based on the assertions, the pattern appears to be:
    The function should calculate (n + 1) * n for the given n.
    Alternatively, if we consider the sequence starting from n=1:
    n=1 -> 0 (1*0)
    n=2 -> 2 (2*1)
    n=3 -> 6 (3*2)
    n=4 -> 12 (4*3) ... but this doesn't match 20.

    Let's re-examine the assertions:
    4 -> 20 = 4 * 5
    5 -> 30 = 5 * 6
    6 -> 42 = 6 * 7

    The pattern is clearly: result = n * (n + 1)

    Args:
        n: An integer representing the position in the rectangular number sequence.

    Returns:
        The n-th rectangular number according to the observed pattern: n * (n + 1).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative (since rectangular numbers are typically defined for non-negative integers).
    """

    # Validate input type
    if not isinstance(n, int):
        raise TypeError(
            f"Input must be an integer, got {type(n).__name__} instead."
        )

    # Validate input value (rectangular numbers are typically defined for non-negative integers)
    # Based on the problem context and typical mathematical definitions,
    # we will allow n >= 0. If n=0, result is 0.
    if n < 0:
        raise ValueError(
            f"Input must be a non-negative integer, got {n} instead."
        )

    # Edge case: zero input
    # While mathematically 0 * 1 = 0 is valid, let's ensure our logic handles it correctly.
    if n == 0:
        return 0

    # Edge case: single element (n=1)
    # Based on our pattern: 1 * 2 = 2
    # This is a valid rectangular number (a 1x2 or 2x1 grid)

    # Calculate the n-th rectangular number using the derived pattern: n * (n + 1)
    # We break this down into explicit steps as requested.

    # Step 1: Calculate the second dimension of the rectangle (n + 1)
    second_dimension = n + 1

    # Step 2: Calculate the area (product of dimensions)
    result = n * second_dimension

    return result