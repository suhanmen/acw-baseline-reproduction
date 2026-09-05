def get_pell(n: int) -> int:
    """
    Calculate the nth Pell number using an iterative approach with explicit validation.

    The Pell numbers are defined by the recurrence relation:
    P(0) = 0
    P(1) = 1
    P(n) = 2 * P(n-1) + P(n-2) for n >= 2

    Parameters:
    n (int): The position in the Pell number sequence (non-negative integer)

    Returns:
    int: The nth Pell number

    Raises:
    TypeError: If n is not an integer
    ValueError: If n is negative

    Edge cases handled:
    - n = 0: Returns 0
    - n = 1: Returns 1
    - Large values: Uses iterative approach to prevent stack overflow
    """

    # Explicit type validation
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    # Explicit range validation
    if n < 0:
        raise ValueError(f"Input must be non-negative, got {n}")

    # Base case: P(0)
    if n == 0:
        return 0

    # Base case: P(1)
    if n == 1:
        return 1

    # Initialize the first two Pell numbers
    prev_pell = 0  # P(0)
    curr_pell = 1  # P(1)

    # Calculate Pell numbers iteratively from 2 up to n
    # We use a loop counter to track our current position
    current_position = 2

    while current_position <= n:
        # Calculate the next Pell number using the recurrence relation
        # P(n) = 2 * P(n-1) + P(n-2)
        next_pell = 2 * curr_pell + prev_pell

        # Update the variables for the next iteration
        # Shift: prev becomes curr, curr becomes next
        prev_pell = curr_pell
        curr_pell = next_pell

        # Increment the position counter
        current_position += 1

    # After the loop completes, curr_pell holds P(n)
    return curr_pell