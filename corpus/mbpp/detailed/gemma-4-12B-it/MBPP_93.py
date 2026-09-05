import math
from typing import Union

def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Calculates the value of a raised to the power of b (a^b).

    This implementation handles:
    - Positive and negative integers/floats for both base and exponent.
    - Zero as a base or exponent.
    - Fractional exponents (resulting in float values).
    - Edge cases like 0^0, 0^negative, and negative bases with fractional exponents.

    Args:
        a (Union[int, float]): The base value.
        b (Union[int, float]): The exponent value.

    Returns:
        Union[int, float]: The result of a raised to the power of b.

    Raises:
        ValueError: If the base is negative and the exponent is a non-integer.
        ZeroDivisionError: If the base is 0 and the exponent is negative.
    """

    # 1. Input Validation: Ensure inputs are numeric types.
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both base 'a' and exponent 'b' must be integers or floats.")

    # 2. Handle 0 raised to a power
    if a == 0:
        if b > 0:
            return 0
        elif b == 0:
            # Mathematically, 0^0 is often undefined, but in most programming 
            # contexts (including Python's pow()), it evaluates to 1.
            return 1
        else:
            # 0 raised to a negative power is equivalent to 1 / (0^|b|),
            # which results in division by zero.
            raise ZeroDivisionError("Cannot raise 0 to a negative power.")

    # 3. Handle negative base with fractional exponent
    # A negative base raised to a fractional exponent results in a complex number.
    # This function is designed for real-number arithmetic.
    is_exponent_integer = float(b).is_integer()
    if a < 0 and not is_exponent_integer:
        raise ValueError("Negative base with a fractional exponent results in a complex number.")

    # 4. Handle Negative Exponents
    # a^-b is equal to 1 / (a^b)
    if b < 0:
        # Calculate the positive power first
        positive_exponent = -b
        base_power = _calculate_power_recursive_or_iterative(a, positive_exponent)
        return 1.0 / base_power

    # 5. Handle Positive/Zero Exponents
    # We use the built-in power operator which is highly optimized for 
    # both integer and float types in Python.
    result = a ** b

    # Ensure we return an int if the inputs were ints and result is a whole number
    # to match the provided assertions (e.g., 3**4 = 81, not 81.0).
    if isinstance(a, int) and isinstance(b, int) and result == int(result):
        return int(result)

    return result

def _calculate_power_recursive_or_iterative(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Helper function to calculate power for positive exponents.
    Specifically used to isolate the logic for internal calculations.
    """
    # Using Python's native exponentiation as it handles precision for floats
    # and efficient multiplication for integers.
    return base ** exponent

# Assertions provided in the problem description
if __name__ == "__main__":
    # The following are provided for verification of requirements.
    assert power(3, 4) == 81
    assert power(2, 3) == 8
    assert power(5, 5) == 3125