import math
import cmath
from typing import Tuple, Union

def convert(number: Union[int, float, complex]) -> Tuple[float, float]:
    """
    Converts a complex number (or an integer/float) into polar coordinates.

    The polar coordinates are returned as a tuple (radius, angle), where:
    - radius (r) is the magnitude (absolute value) of the complex number.
    - angle (theta) is the phase angle in radians, ranging from -pi to pi.

    Args:
        number: An int, float, or complex number to convert.

    Returns:
        A tuple of two floats (radius, angle).

    Raises:
        TypeError: If the input is not a numeric type (int, float, complex).
        ValueError: If the input is NaN or Infinity.
    """

    # Validate input type
    # We accept int, float, and complex types.
    if not isinstance(number, (int, float, complex)):
        raise TypeError(f"Input must be a numeric type (int, float, complex), "
                        f"but received {type(number).__name__}.")

    # Cast to complex to ensure uniform processing
    # This handles integers and floats by treating them as having an imaginary part of 0.
    complex_num = complex(number)

    # Handle non-finite numbers (NaN and Infinity)
    # These cannot be converted to standard polar coordinates.
    if not math.isfinite(complex_num.real) or not math.isfinite(complex_num.imag):
        raise ValueError("Input must be a finite number (cannot be NaN or Infinity).")

    # Step 1: Calculate the magnitude (radius)
    # The magnitude r = sqrt(x^2 + y^2).
    # cmath.polar returns (r, phi). We can extract r directly.
    # Using cmath.abs() is the standard way to get the magnitude of a complex number.
    radius: float = abs(complex_num)

    # Step 2: Calculate the phase angle (theta)
    # The angle is measured in radians from the positive real axis.
    # cmath.phase returns the angle in the range (-pi, pi].
    angle: float = cmath.phase(complex_num)

    # Special case handling for zero
    # If the input is 0 + 0j, the magnitude is 0.0. 
    # The phase is mathematically undefined, but cmath.phase returns 0.0.
    if radius == 0.0:
        # We ensure precision for 0.0 cases.
        return (0.0, 0.0)

    # Return the result as a tuple of floats
    return (float(radius), float(angle))

# The problem asks for the following assertions to be satisfied:
# assert convert(1) == (1.0, 0.0)
# assert convert(4) == (4.0,0.0)
# assert convert(5) == (5.0,0.0)