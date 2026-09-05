from typing import Union

Number = Union[int, float]


def _validate_input(n: Number) -> None:
    """
    Validates that the input 'n' is a valid positive integer.

    Rules:
    1. Must be an integer type (or a float that represents an integer).
    2. Must be strictly positive (n > 0).

    Raises:
        TypeError: If 'n' is not an integer or float.
        ValueError: If 'n' is not a positive integer.
    """
    # Check for type validity
    if not isinstance(n, (int, float)):
        raise TypeError(f"Input must be a number, got {type(n).__name__}.")

    # Handle float representation of integers (e.g., 4.0)
    # We convert to int if it's a whole number float, but we must check value first.
    if isinstance(n, float):
        if not n.is_integer():
            raise TypeError(f"Input must be an integer, got a non-integer float {n}.")
        # Convert to int for further processing logic
        n = int(n)

    # Check for positive constraint
    if n <= 0:
        raise ValueError(f"Input must be a positive integer, got {n}.")


def _calculate_harmonic_sum(n: int) -> float:
    """
    Calculates the harmonic sum for n-1.

    The harmonic series is defined as: H_k = 1/1 + 1/2 + ... + 1/k.
    This function calculates H_{n-1}.

    Args:
        n: A positive integer representing the upper bound parameter.

    Returns:
        The sum of the harmonic series up to term (n-1).
        Returns 0.0 if n-1 is 0 (i.e., n=1).
    """
    # Determine the actual number of terms to sum
    upper_bound = n - 1

    # Edge case: if the sequence is empty (n=1), the sum is 0
    if upper_bound <= 0:
        return 0.0

    total_sum: float = 0.0
    term: float = 0.0

    # Explicit loop to calculate sum to maintain clarity and allow debugging
    for i in range(1, upper_bound + 1):
        term = 1.0 / float(i)
        total_sum = total_sum + term

    return total_sum


def harmonic_sum(n: Number) -> float:
    """
    Calculates the harmonic sum of n-1.

    This function computes the sum of the series: 1/1 + 1/2 + ... + 1/(n-1).

    Args:
        n: A positive integer indicating the sequence parameter.

    Returns:
        float: The calculated harmonic sum.

    Raises:
        TypeError: If 'n' is not an integer or valid numeric type.
        ValueError: If 'n' is not positive.

    Examples:
        >>> harmonic_sum(1)
        0.0
        >>> harmonic_sum(2)
        1.0
        >>> harmonic_sum(4)
        2.083333333333333
        >>> harmonic_sum(7)
        2.5928571428571425
    """
    _validate_input(n)
    return _calculate_harmonic_sum(n)