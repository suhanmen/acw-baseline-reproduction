def get_pell(n):
    """
    Calculate the nth Pell number.

    Pell numbers follow the recurrence relation P(n) = 2*P(n-1) + P(n-2)
    with P(0) = 0 and P(1) = 1.

    Args:
        n (int): The index of the Pell number to calculate.

    Returns:
        int: The nth Pell number if n is a non-negative integer.
        None: If n is negative or not an integer.
    """
    # Input validation: Check if n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        return None

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Initialize the first two Pell numbers
        p_prev_prev = 0  # P(n-2)
        p_prev = 1       # P(n-1)

        for _ in range(2, n + 1):
            # Calculate the next Pell number
            current = 2 * p_prev + p_prev_prev
            # Update the previous values for the next iteration
            p_prev_prev, p_prev = p_prev, current

        return current