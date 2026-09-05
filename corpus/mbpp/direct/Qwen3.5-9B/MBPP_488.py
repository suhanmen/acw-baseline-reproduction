import math

def area_pentagon(side):
    """Calculate the area of a regular pentagon given the side length."""
    return (5 * side ** 2) / (4 * math.tan(math.pi / 5))