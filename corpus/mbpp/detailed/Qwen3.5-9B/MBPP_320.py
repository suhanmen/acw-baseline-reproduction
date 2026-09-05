def _validate_n(n):
    """
    Validates that the input n is a non-negative integer.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError(f"Input must be an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError(f"Input must be a non-negative integer, got {n}")

def _compute_sum_of_first_n(n):
    """
    Computes the sum of the first n natural numbers.

    Formula: S = n * (n + 1) / 2

    Returns:
        int: The sum of the first n natural numbers.
    """
    return (n * (n + 1)) // 2

def _compute_square_of_sum(n):
    """
    Computes the square of the sum of the first n natural numbers.

    Steps:
    1. Calculate the sum of the first n natural numbers.
    2. Square the result.

    Returns:
        int: The square of the sum.
    """
    total_sum = _compute_sum_of_first_n(n)
    return total_sum * total_sum

def _compute_sum_of_squares(n):
    """
    Computes the sum of the squares of the first n natural numbers.

    Formula: Sum = n * (n + 1) * (2n + 1) / 6

    Returns:
        int: The sum of the squares.
    """
    return (n * (n + 1) * (2 * n + 1)) // 6

def sum_difference(n):
    """
    Calculates the difference between the squared sum of the first n natural numbers
    and the sum of the squares of the first n natural numbers.

    Mathematical definition:
        Result = (Sum of first n numbers)^2 - (Sum of squares of first n numbers)

    Examples:
        For n = 12:
            Sum of first 12 = 78
            Square of Sum = 78^2 = 6084
            Sum of Squares = 1^2 + ... + 12^2 = 650
            Difference = 6084 - 650 = 5434

    Args:
        n (int): The number of natural numbers to consider. Must be >= 0.

    Returns:
        int: The calculated difference.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.
    """
    # Step 1: Validate the input
    _validate_n(n)

    # Step 2: Handle the edge case where n is 0
    # The sum of zero numbers is 0.
    # Square of sum is 0. Sum of squares is 0. Difference is 0.
    if n == 0:
        return 0

    # Step 3: Calculate the square of the sum of the first n natural numbers
    squared_sum_result = _compute_square_of_sum(n)

    # Step 4: Calculate the sum of the squares of the first n natural numbers
    sum_of_squares_result = _compute_sum_of_squares(n)

    # Step 5: Calculate the difference
    difference = squared_sum_result - sum_of_squares_result

    return difference