import math
from typing import Union

def round_num(number: Union[int, float], multiple: Union[int, float]) -> Union[int, float]:
    """
    Rounds a given number to the nearest multiple of a specific value.

    If the number is exactly halfway between two multiples, this implementation
    rounds towards the nearest even multiple (standard rounding behavior)
    or simply rounds to the closest integer multiple.

    Args:
        number: The input number to be rounded.
        multiple: The multiple to which the number should be rounded.

    Returns:
        The number rounded to the nearest multiple.

    Raises:
        ValueError: If the multiple is zero (division by zero is undefined).
        TypeError: If inputs are not numeric.
    """
    # Validate that inputs are numeric
    if not isinstance(number, (int, float)) or not isinstance(multiple, (int, float)):
        raise TypeError("Both 'number' and 'multiple' must be integers or floats.")

    # Validate that multiple is not zero to prevent division by zero
    if multiple == 0:
        raise ValueError("The 'multiple' cannot be zero.")

    # Handle the case where the number is already a multiple
    # We use a small epsilon for float comparisons to handle precision issues
    remainder = number % multiple
    if math.isclose(remainder, 0, abs_tol=1e-9) or math.isclose(remainder, multiple, abs_tol=1e-9):
        return number

    # Determine how many times the multiple fits into the number
    # We use float division to ensure we capture the fractional part
    fractional_count = number / multiple

    # Round the fractional count to the nearest integer
    # The built-in round() function in Python 3 rounds to the nearest 
    # even number for .5 cases, which is standard for "nearest" rounding.
    rounded_count = round(fractional_count)

    # Calculate the final rounded number
    result = rounded_count * multiple

    # Return as an integer if both inputs were integers and result is whole
    if isinstance(number, int) and isinstance(multiple, int):
        return int(result)

    return result

# The following assertions are provided to verify the requirements:
# assert round_num(4722, 10) == 4720
# assert round_num(1111, 5) == 1110
# assert round_num(219, 2) == 218