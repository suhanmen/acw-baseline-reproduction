import math
import typing


def _validate_positive_integer(number: int) -> None:
    """
    Validates that the input is a positive integer (greater than 0).

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
    """
    if not isinstance(number, int):
        raise TypeError(f"Expected an integer, got {type(number).__name__}")

    if number <= 0:
        raise ValueError(f"Expected a positive integer (greater than 0), got {number}")


def _compute_highest_power_of_2_less_than_equal_to(number: int) -> int:
    """
    Calculates the highest power of 2 less than or equal to the given number.

    This function uses the logarithm base 2 approach for calculation:
    1. It calculates log2(number).
    2. It takes the floor of that result to get the exponent.
    3. It computes 2 raised to that exponent.

    This approach is robust for large integers handled by Python's arbitrary precision
    and avoids potential infinite loops associated with manual bit-shifting.

    Args:
        number: A positive integer.

    Returns:
        The highest power of 2 less than or equal to 'number'.

    Example:
        If number is 10:
        log2(10) ≈ 3.32
        floor(3.32) = 3
        2^3 = 8
        Returns 8.
    """
    # Calculate the base-2 logarithm of the number
    log_value = math.log(number, 2)

    # Get the integer part (floor) of the logarithm.
    # This represents the exponent of the highest power of 2 less than or equal to the number.
    exponent = int(math.floor(log_value))

    # Compute 2 raised to the calculated exponent.
    result = 1 << exponent

    return result


def highest_Power_of_2(number: int) -> int:
    """
    Finds the highest power of 2 less than or equal to the given number.

    This function serves as the main interface. It performs strict input validation
    before delegating the calculation logic to a dedicated helper function.

    Args:
        number: An integer representing the upper bound.

    Returns:
        An integer representing the highest power of 2 less than or equal to 'number'.

    Raises:
        TypeError: If 'number' is not an instance of int.
        ValueError: If 'number' is less than or equal to 0.

    Examples:
        >>> highest_Power_of_2(10)
        8
        >>> highest_Power_of_2(19)
        16
        >>> highest_Power_of_2(32)
        32
        >>> highest_Power_of_2(1)
        1
        >>> highest_Power_of_2(0)
        Traceback (most recent call last):
            ...
        ValueError: Expected a positive integer (greater than 0), got 0
    """
    _validate_positive_integer(number)

    return _compute_highest_power_of_2_less_than_equal_to(number)