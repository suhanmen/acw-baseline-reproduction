def _is_valid_index(n: int) -> bool:
    """
    Check if the given index n is a valid non-negative integer.
    Returns True if valid, False otherwise.
    """
    if not isinstance(n, int):
        return False
    return n >= 0


def _calculate_perrin_recursive(n: int) -> int:
    """
    Helper function to calculate the n-th Perrin number using direct recursion.

    The Perrin sequence is defined as:
    P(0) = 3
    P(1) = 0
    P(2) = 2
    P(n) = P(n-2) + P(n-3) for n > 2

    This function relies on the base cases being handled by the caller 
    (or by this function for n <= 2) to avoid infinite recursion.
    For indices 0, 1, and 2, it returns the constant values directly.
    For indices greater than 2, it recursively calls itself.
    """
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2

    # For n > 2, apply the recurrence relation: P(n) = P(n-2) + P(n-3)
    # We calculate the two required components recursively.
    term_1 = _calculate_perrin_recursive(n - 2)
    term_2 = _calculate_perrin_recursive(n - 3)

    return term_1 + term_2


def get_perrin(n: int) -> int:
    """
    Find the n'th Perrin number using recursion.

    Input validation:
    - n must be an integer.
    - n must be non-negative (>= 0).

    If n is invalid, a ValueError is raised explicitly.

    Valid behavior:
    - P(0) = 3
    - P(1) = 0
    - P(2) = 2
    - P(n) = P(n-2) + P(n-3) for n > 2

    Examples:
    - get_perrin(9) -> 12
    - get_perrin(4) -> 2
    - get_perrin(6) -> 5
    """
    # Step 1: Validate the input type and value explicitly.
    if not _is_valid_index(n):
        raise ValueError(
            f"Invalid input n={n}. n must be a non-negative integer."
        )

    # Step 2: Delegate the actual recursive calculation to the helper function.
    return _calculate_perrin_recursive(n)