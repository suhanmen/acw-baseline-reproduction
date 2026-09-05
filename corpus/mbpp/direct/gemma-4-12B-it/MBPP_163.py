import math

def area_polygon(n: int, s: float) -> float:
    """
    Calculates the area of a regular polygon with n sides of length s.
    The formula is: Area = (n * s^2) / (4 * tan(pi / n))
    """
    area = (n * s**2) / (4 * math.tan(math.pi / n))
    return area