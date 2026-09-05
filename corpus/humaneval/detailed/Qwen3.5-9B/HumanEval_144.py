import math

def _parse_fraction(fraction_string):
    """
    Parses a fraction string in the format 'numerator/denominator'.

    Returns a tuple of (numerator, denominator) as integers.
    Raises ValueError if the string is invalid.
    """
    if not isinstance(fraction_string, str):
        raise ValueError("Fraction must be a string.")

    if "/" not in fraction_string:
        raise ValueError(f"Invalid fraction format: missing separator '/'. Got: '{fraction_string}'")

    parts = fraction_string.split("/")
    if len(parts) != 2:
        raise ValueError(f"Invalid fraction format: expected exactly one '/', found: '{fraction_string}'")

    numerator_str, denominator_str = parts

    if not numerator_str or not denominator_str:
        raise ValueError("Numerator and denominator cannot be empty.")

    try:
        numerator = int(numerator_str)
        denominator = int(denominator_str)
    except ValueError:
        raise ValueError(f"Invalid integer format in fraction: '{fraction_string}'")

    return numerator, denominator

def _multiply_fractions(n1, d1, n2, d2):
    """
    Multiplies two fractions (n1/d1) * (n2/d2).

    Returns the result as a tuple of (result_numerator, result_denominator) in simplified form.
    Uses GCD to simplify the result immediately after multiplication.
    """
    # Multiply numerators and denominators
    result_numerator = n1 * n2
    result_denominator = d1 * d2

    # Simplify the result fraction by dividing by GCD
    common_divisor = math.gcd(result_numerator, result_denominator)
    simplified_numerator = result_numerator // common_divisor
    simplified_denominator = result_denominator // common_divisor

    return simplified_numerator, simplified_denominator

def _is_whole_number(numerator, denominator):
    """
    Checks if the fraction numerator/denominator represents a whole number.

    A fraction is a whole number if the denominator divides the numerator evenly.
    Assumes denominator is positive.
    """
    if denominator == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")

    # If denominator is 1, it is always a whole number
    if denominator == 1:
        return True

    # Check divisibility
    return numerator % denominator == 0

def simplify(x, n):
    """
    Determines if the product of two fractions represented as strings evaluates to a whole number.

    Args:
        x (str): A string representing a fraction (e.g., "1/5").
        n (str): A string representing a fraction (e.g., "5/1").

    Returns:
        bool: True if x * n is a whole number, False otherwise.

    Raises:
        ValueError: If input strings are not in valid fraction format.
    """
    # Validate inputs are strings
    if not isinstance(x, str) or not isinstance(n, str):
        raise ValueError("Both arguments must be strings.")

    # Check for empty strings
    if not x or not n:
        raise ValueError("Fraction strings cannot be empty.")

    # Parse the first fraction
    try:
        n1, d1 = _parse_fraction(x)
    except ValueError as e:
        raise ValueError(f"Invalid input 'x': {e}") from e

    # Parse the second fraction
    try:
        n2, d2 = _parse_fraction(n)
    except ValueError as e:
        raise ValueError(f"Invalid input 'n': {e}") from e

    # Validate constraints: numerators and denominators must be positive whole numbers
    if n1 <= 0 or d1 <= 0 or n2 <= 0 or d2 <= 0:
        raise ValueError("Numerators and denominators must be positive whole numbers.")

    # Multiply the fractions
    result_numerator, result_denominator = _multiply_fractions(n1, d1, n2, d2)

    # Check if the result is a whole number
    is_whole = _is_whole_number(result_numerator, result_denominator)

    return is_whole