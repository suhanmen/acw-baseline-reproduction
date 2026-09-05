def babylonian_squareroot(a):
    """
    Compute the square root of a non-negative number using the Babylonian method.

    Args:
        a (float or int): The number to compute the square root of. Must be non-negative.

    Returns:
        float: The square root of a.

    Raises:
        ValueError: If a is negative.
    """
    # Input validation
    if not isinstance(a, (int, float)):
        raise ValueError("Input must be a number")
    if a < 0:
        raise ValueError("Cannot compute square root of a negative number")

    # Handle the case where a is 0
    if a == 0:
        return 0.0

    # Base case for 1 since sqrt(1) is 1
    if a == 1:
        return 1.0

    # Initial guess
    x = a / 2.0

    # Tolerance for stopping condition
    tolerance = 1e-10

    # Previous value to track change
    prev = 0.0

    while True:
        # Compute next guess using the Babylonian formula
        prev, x = x, (prev + a / x) / 2.0

        # Check if the change is below the tolerance
        if abs(x - prev) < tolerance:
            return x

        # Prevent infinite looping in case of unexpected behavior
        if prev == 0:
            return 0.0

        # If the value gets too large, it means it's diverging
        if x > 1e6:
            return x

    return x