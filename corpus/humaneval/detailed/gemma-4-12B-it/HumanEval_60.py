import typing

def _validate_input_is_integer(value: typing.Any) -> None:
    """
    Validates that the input provided is of type int.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(value, int):
        raise TypeError(f"Input must be an integer. Received: {type(value).__name__}")

def _validate_positive_range(value: int) -> None:
    """
    Validates that the integer is at least 1.

    Raises:
        ValueError: If the input is less than 1.
    """
    if value < 1:
        raise ValueError(f"Input must be a positive integer greater than or equal to 1. Received: {value}")

def sum_to_n(n: int) -> int:
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    # Step 1: Validate that the input is actually an integer.
    _validate_input_is_integer(n)

    # Step 2: Validate that the input is within the logical bounds for the problem.
    # Since the problem asks for sums from 1 to n, n must be >= 1.
    _validate_positive_range(n)

    # Step 3: Handle the calculation logic.
    # We can use the arithmetic series formula: Sum = (n * (n + 1)) / 2
    # This is O(1) complexity and more efficient than a loop for very large n.

    # Calculate the number of terms
    num_terms: int = n

    # Calculate the sum of the first and last terms
    first_term: int = 1
    last_term: int = n

    # Calculate the sum using the standard arithmetic progression formula
    # We use floor division // to ensure the result remains an integer type.
    total_sum: int = (num_terms * (first_term + last_term)) // 2

    return total_sum