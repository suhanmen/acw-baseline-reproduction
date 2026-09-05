import math

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.

    If the input is 0, the function returns 0.0.
    If the input is negative or not a valid number, a ValueError is raised.

    >>> truncate_number(3.5)
    0.5

    >>> truncate_number(5.0)
    0.0

    >>> truncate_number(0.0)
    0.0
    """
    if not isinstance(number, float):
        raise ValueError("Input must be a float.")
    if not math.isfinite(number):
        raise ValueError("Input must be a finite number.")
    if number < 0:
        raise ValueError("Input must be a positive number.")

    if number == 0:
        return 0.0

    integer_part = math.floor(number)
    decimal_part = number - integer_part

    return decimal_part