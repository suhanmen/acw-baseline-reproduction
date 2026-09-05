def sum_series(n):
    """
    Calculates the sum of the arithmetic series: n + (n-2) + (n-4) + ... 
    The series continues until the next term would be less than or equal to zero.

    Parameters:
        n (int): The starting integer of the series.

    Returns:
        int: The calculated sum of the positive terms in the series.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is negative (as no positive terms exist).

    Examples:
        sum_series(6) -> 6 + 4 + 2 = 12
        sum_series(10) -> 10 + 8 + 6 + 4 + 2 = 30
        sum_series(9) -> 9 + 7 + 5 + 3 + 1 = 25
    """

    # --- Input Validation ---

    # Check for type correctness
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, received type: {type(n).__name__}")

    # Check for negative numbers explicitly
    # Since the problem asks for "positive integers", a negative starting point
    # yields no terms and thus no sum. We raise an error to be explicit.
    if n < 0:
        raise ValueError(f"Input must be non-negative, received: {n}")

    # Handle the zero case explicitly
    # If n is 0, the series is 0 (which is not positive), so the sum is 0.
    if n == 0:
        return 0

    # --- Series Calculation ---

    # Initialize the accumulator for the total sum
    total_sum = 0

    # Initialize the current term variable
    current_term = n

    # Loop while the current term is strictly greater than 0
    # This ensures we only add positive integers as required.
    while current_term > 0:
        # Add the current term to the running total
        total_sum = total_sum + current_term

        # Calculate the next term by subtracting 2
        current_term = current_term - 2

    # Return the final calculated sum
    return total_sum