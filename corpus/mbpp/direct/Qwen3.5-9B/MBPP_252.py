import cmath
import math

def convert(z):
    if not isinstance(z, complex):
        z = complex(z)
    r = abs(z)
    theta = cmath.phase(z)
    return (float(r), float(theta))