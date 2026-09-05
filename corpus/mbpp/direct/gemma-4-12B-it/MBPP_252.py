import math
import cmath

def convert(z: complex) -> tuple[float, float]:
    """
    Converts a complex number to polar coordinates (magnitude, angle).

    Args:
        z: A complex number (e.g., 1, 1+1j, 5).

    Returns:
        A tuple (r, theta) where r is the magnitude and theta is the angle in radians.
    """
    r, phi = cmath.polar(z)
    # The assertions require 0.0 instead of -0.0 for real numbers.
    # cmath.polar can sometimes return -0.0 for positive real numbers.
    if phi == -0.0:
        phi = 0.0
    return (float(r), float(phi))

if __name__ == "__main__":
    assert convert(1) == (1.0, 0.0)
    assert convert(4) == (4.0, 0.0)
    assert convert(5) == (5.0, 0.0)