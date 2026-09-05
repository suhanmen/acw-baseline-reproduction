def _validate_input(n: int) -> None:
    """
    Validates that the input n is a valid positive integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a positive integer (must be >= 1).
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 1:
        raise ValueError(f"Input must be a positive integer (n >= 1), got {n}")


def _compute_nth_octagonal_number(n: int) -> int:
    """
    Computes the nth octagonal number using the explicit formula.

    The formula for the nth octagonal number is:
    O_n = n * (3*n - 2)

    Args:
        n (int): The position in the sequence of octagonal numbers (1-indexed).

    Returns:
        int: The nth octagonal number.
    """
    # Step 1: Calculate the linear term (3 * n)
    linear_term = 3 * n

    # Step 2: Subtract 2 from the linear term
    bracket_term = linear_term - 2

    # Step 3: Multiply n by the result of the bracket term
    result = n * bracket_term

    return result


def is_octagonal(n: int) -> int:
    """
    Finds the nth octagonal number.

    This function acts as a wrapper that validates the input and then 
    computes the nth octagonal number using the standard mathematical formula.

    The sequence of octagonal numbers starts as follows:
    n=1 -> 1
    n=2 -> 8
    n=3 -> 21
    n=4 -> 40
    n=5 -> 65
    ...

    Args:
        n (int): The index of the octagonal number to retrieve (must be >= 1).

    Returns:
        int: The nth octagonal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not a positive integer.
    """
    # Step 1: Validate the input to ensure it meets all requirements
    _validate_input(n)

    # Step 2: Compute the value using the dedicated helper function
    octagonal_value = _compute_nth_octagonal_number(n)

    # Step 3: Return the computed value
    return octagonal_value