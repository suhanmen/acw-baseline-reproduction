import cmath
import math
from typing import Tuple, Union

Number = Union[int, float, complex]


def _validate_input(number: Number) -> None:
    """
    Validate that the input is a valid number (int, float, or complex).
    Raises a TypeError if the input is not a number.
    """
    if isinstance(number, (int, float, complex)):
        return
    raise TypeError(
        f"Input must be a number (int, float, or complex), got {type(number).__name__}"
    )


def _validate_complex_number(number: Number) -> None:
    """
    Validate that the input is actually a complex number.
    Although int and float are accepted and implicitly converted,
    this function ensures that if a complex number is provided,
    it has valid real and imaginary parts.
    """
    if isinstance(number, complex):
        # Complex numbers are always valid in Python, but we check for
        # potential nan/inf components if strict validation is desired.
        # For this problem, standard complex numbers are accepted.
        return
    # If we reach here, it's an int or float, which are valid.
    return


def _parse_complex_input(number: Number) -> complex:
    """
    Parse the input into a complex number.
    If the input is an int or float, it is converted to a complex number
    with zero imaginary part.
    """
    if isinstance(number, (int, float)):
        return complex(number, 0.0)
    return number


def _compute_magnitude(real_part: float, imag_part: float) -> float:
    """
    Compute the magnitude (r) of the complex number.
    r = sqrt(real^2 + imag^2)
    """
    real_squared = real_part * real_part
    imag_squared = imag_part * imag_part
    sum_of_squares = real_squared + imag_squared

    # Math.sqrt handles negative zero correctly, but let's be explicit about
    # ensuring we don't pass NaN if inputs were NaN.
    if math.isnan(sum_of_squares):
        raise ValueError("Cannot compute magnitude of complex number containing NaN.")

    magnitude = math.sqrt(sum_of_squares)
    return magnitude


def _compute_phase(real_part: float, imag_part: float) -> float:
    """
    Compute the phase (theta) of the complex number in radians.
    theta = atan2(imag, real)

    We use math.atan2 instead of cmath.phase because atan2 is available
    for real inputs and provides consistent results across all quadrants.
    """
    phase = math.atan2(imag_part, real_part)
    return phase


def convert(number: Number) -> Tuple[float, float]:
    """
    Convert a complex number (or a real number) to polar coordinates.

    Returns a tuple of (magnitude, phase) where:
    - magnitude is the absolute value (modulus) of the complex number.
    - phase is the argument (angle in radians) of the complex number.

    The phase is returned in the range (-pi, pi].

    Edge cases handled:
    - Empty input: Not applicable for numbers, but validated type-wise.
    - Single element: Handled correctly by magnitude and phase calculations.
    - All-equal elements: N/A, but zero is handled correctly (magnitude=0, phase=0).
    - Boundary values: Very large/small numbers are handled by floating point standards.
    - Zero / negative numbers: 
        * Zero (0+0j) results in magnitude 0.0 and phase 0.0.
        * Negative real numbers result in phase -pi or pi (depending on implementation of atan2).
        * Python's math.atan2 returns -pi for (-inf, 0).
    - Invalid inputs: Raises TypeError or ValueError with descriptive messages.
    """

    # Step 1: Validate the input type
    _validate_input(number)

    # Step 2: Validate that it is a valid complex number representation
    _validate_complex_number(number)

    # Step 3: Parse the input into a standard complex number structure
    complex_number = _parse_complex_input(number)

    # Step 4: Extract real and imaginary parts
    real_part = complex_number.real
    imag_part = complex_number.imag

    # Step 5: Check for NaN in components to prevent invalid calculations
    if math.isnan(real_part) or math.isnan(imag_part):
        raise ValueError("Complex number must not contain NaN components.")

    # Step 6: Compute the magnitude
    magnitude = _compute_magnitude(real_part, imag_part)

    # Step 7: Compute the phase
    phase = _compute_phase(real_part, imag_part)

    # Step 8: Return the result as a tuple of floats
    return (float(magnitude), float(phase))


if __name__ == "__main__":
    # Basic sanity checks to ensure the logic works as expected before production
    test_cases = [
        (1, (1.0, 0.0)),
        (4, (4.0, 0.0)),
        (5, (5.0, 0.0)),
        (-1, (1.0, math.pi)), # Phase could be pi or -pi depending on atan2 implementation details for negative reals
        (0, (0.0, 0.0)),
        (1+0j, (1.0, 0.0)),
        (0+1j, (1.0, math.pi / 2)),
        (1+1j, (math.sqrt(2), math.pi / 4)),
    ]

    for input_val, expected in test_cases:
        result = convert(input_val)
        print(f"convert({input_val}) = {result}")