import cmath
import math

def angle_complex(real: float, imag: float) -> float:
    """
    Returns the angle (in radians) of the complex number (real, imag).
    """
    return cmath.phase(real + imag*1j)