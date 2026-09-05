def get_carol(n):
    """
    Calculate the n-th Carol number.

    Carol numbers are defined by the formula: C_n = (2^n - 1)^2 - 2.
    This function handles all valid inputs and raises appropriate errors for invalid ones.

    Args:
        n (int): The position in the Carol sequence. Must be a positive integer.

    Returns:
        int: The n-th Carol number.

    Raises:
        ValueError: If n is not an integer, is zero, or is negative.
    """
    # Input validation
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

    # Helper function to calculate 2^k
    def power_of_two(k):
        """
        Compute 2 raised to the power of k.

        Args:
            k (int): The exponent.

        Returns:
            int: 2^k
        """
        result = 1
        for _ in range(k):
            result *= 2
        return result

    # Calculate 2^n
    two_power_n = power_of_two(n)

    # Calculate (2^n - 1)
    minus_one = two_power_n - 1

    # Square the result
    squared = minus_one ** 2

    # Subtract 2 to get the Carol number
    carol_number = squared - 2

    return carol_number