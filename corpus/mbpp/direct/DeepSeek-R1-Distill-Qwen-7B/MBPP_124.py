python
import math

def angle_complex(x: float, y: complex) -> float:
    # Calculate the argument (angle) of the complex number x + yj
    # Using the math.atan2 function which takes y and x as arguments
    # and returns the angle in radians between -pi and pi
    return math.atan2(y, x)