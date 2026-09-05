def is_valid_positive_integer(value):
    """
    Validates that the input is a positive integer (>= 1).

    Returns True if valid, raises ValueError otherwise.
    """
    if not isinstance(value, int):
        raise ValueError(f"Input must be an integer, got {type(value).__name__}")

    if value < 1:
        raise ValueError(f"Input must be a positive integer (>= 1), got {value}")

    return True


def calculate_hexagonal_number(n):
    """
    Calculates the nth hexagonal number using the formula:
    H(n) = n * (2 * n - 1)

    This function performs the calculation step-by-step with named variables
    for clarity and maintainability.

    Args:
        n (int): The position of the hexagonal number to calculate (1-based index).

    Returns:
        int: The nth hexagonal number.

    Raises:
        ValueError: If n is not a valid positive integer.
    """
    # Step 1: Validate the input
    is_valid_positive_integer(n)

    # Step 2: Calculate the term (2 * n - 1) explicitly
    term_two_n_minus_one = (2 * n) - 1

    # Step 3: Calculate the final result by multiplying n by the term calculated in step 2
    hexagonal_result = n * term_two_n_minus_one

    return hexagonal_result


def hexagonal_num(n):
    """
    Public function to find the nth hexagonal number.

    This function serves as the main entry point and delegates the calculation
    and validation logic to helper functions for modularity and clarity.

    Args:
        n (int): The position of the hexagonal number to find.

    Returns:
        int: The nth hexagonal number.

    Raises:
        ValueError: If the input n is not a valid positive integer.

    Examples:
        >>> hexagonal_num(10)
        190
        >>> hexagonal_num(5)
        45
        >>> hexagonal_num(7)
        91
    """
    return calculate_hexagonal_number(n)