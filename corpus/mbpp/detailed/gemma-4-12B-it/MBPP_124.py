import math
from typing import Union

def angle_complex(real_part: Union[float, complex], imag_part: Union[float, complex]) -> float:
    """
    Calculates the angle of a complex number formed by combining two components.

    The first argument is the real component (can be a float or complex).
    The second argument is the imaginary component (can be a float or complex).
    The function sums the real and imaginary parts of both arguments to find 
    the final complex number and returns its phase angle.
    """

    # Validation for input types
    valid_types = (float, int, complex)
    if not isinstance(real_part, valid_types):
        raise TypeError(f"real_part must be float, int, or complex. Got {type(real_part)}")
    if not isinstance(imag_part, valid_types):
        raise TypeError(f"imag_part must be float, int, or complex. Got {type(imag_part)}")

    # Extract real and imaginary parts from the first input
    if isinstance(real_part, complex):
        real_component_1 = real_part.real
        imag_component_1 = real_part.imag
    else:
        real_component_1 = float(real_part)
        imag_component_1 = 0.0

    # Extract real and imaginary parts from the second input
    if isinstance(imag_part, complex):
        real_component_2 = imag_part.real
        imag_component_2 = imag_part.imag
    else:
        real_component_2 = float(imag_part)
        imag_component_2 = 0.0

    # Combine the components to form the final complex number:
    # The input structure angle_complex(r, i) implies:
    # Result = r + i
    # If r is complex, Result = r.real + r.imag*j + i
    # If i is complex, Result = r + i.real + i.imag*j
    # Thus, we sum all real parts and all imaginary parts.

    final_real = real_component_1 + real_component_2
    final_imag = imag_component_1 + imag_component_2

    # Handle the origin (0,0) case
    if final_real == 0.0 and final_imag == 0.0:
        return 0.0

    # Use atan2 to get the angle in the range (-pi, pi]
    # math.atan2 takes (y, x)
    angle = math.atan2(final_imag, final_real)

    return angle