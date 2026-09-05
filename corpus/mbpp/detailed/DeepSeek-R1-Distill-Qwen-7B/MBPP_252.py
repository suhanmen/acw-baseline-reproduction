import math

def convert(complex_number):
    """
    Convert a complex number to polar coordinates (r, theta).

    Parameters:
        complex_number (complex): A complex number to be converted.

    Returns:
        tuple: A tuple containing the magnitude (r) and angle (theta) in radians.

    Raises:
        ValueError: If the input is not a valid complex number or has invalid values.
    """
    if not isinstance(complex_number, complex):
        raise ValueError("Invalid input: must be a complex number.")

    a = complex_number.real
    b = complex_number.imag

    if a == 0 and b == 0:
        return (0.0, 0.0)

    r = math.hypot(a, b)
    theta = math.atan2(b, a)

    return (r, theta)

# Test the function with the given assertions
assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0, 0.0)
assert convert(5) == (5.0, 0.0)