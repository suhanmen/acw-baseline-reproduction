import math

def validate_input(value):
    """
    Validates that the input is a positive integer.

    Parameters:
        value (int): The input value to check.

    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is not a positive integer (must be > 0).
    """
    if not isinstance(value, int):
        raise TypeError(f"Expected an integer, got {type(value).__name__}.")

    if value <= 0:
        raise ValueError(f"Input must be a positive integer greater than 0, got {value}.")

    return True

def find_divisor_count(n):
    """
    Calculates the number of divisors of a positive integer n.

    This function uses the property that divisors come in pairs.
    We iterate from 1 up to the square root of n. If i is a divisor,
    then n // i is also a divisor.

    Special handling is applied for perfect squares to avoid double counting.

    Parameters:
        n (int): A positive integer for which to count divisors.

    Returns:
        int: The total number of divisors of n.
    """
    if n == 1:
        # Edge case: 1 has exactly one divisor, which is 1 itself.
        return 1

    count = 0
    limit = int(math.isqrt(n))

    i = 1
    while i <= limit:
        if n % i == 0:
            quotient = n // i
            count += 1

            if i != quotient:
                count += 1
        i += 1

    return count

def divisor(number):
    """
    Main entry point to find the number of divisors of a given integer.

    This function handles input validation and calls the core logic.

    Parameters:
        number (int): The integer for which to count divisors.

    Returns:
        int: The number of divisors.

    Raises:
        TypeError: If 'number' is not an integer.
        ValueError: If 'number' is not a positive integer.
    """
    validate_input(number)
    return find_divisor_count(number)