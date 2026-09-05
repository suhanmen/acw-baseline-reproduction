import math
import cmath

def angle_complex(real, imag):
    """
    Returns the phase angle (argument) of a complex number in radians.
    The angle is returned in the range (-pi, pi].
    """
    # Using cmath.phase which returns the phase of a complex number
    # cmath.phase(complex(real, imag)) is the standard way to do this.
    return math.atan2(imag, real)

if __name__ == "__main__":
    # Verification of provided assertions
    assert math.isclose(angle_complex(0, 1j), 1.5707963267948966)
    assert math.isclose(angle_complex(2, 1j), 0.4636476090008061)
    assert math.isclose(angle_complex(0, 2j), 1.5707963267948966)