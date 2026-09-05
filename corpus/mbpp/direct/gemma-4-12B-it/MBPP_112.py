import math

def perimeter(radius, height):
    """
    Calculates the perimeter of a cylinder.
    Based on the provided assertions:
    perimeter(2,4) == 12 -> (2 * 2) + (2 * 4) = 4 + 8 = 12
    perimeter(1,2) == 6 -> (2 * 1) + (2 * 2) = 2 + 4 = 6
    perimeter(3,1) == 8 -> (2 * 3) + (2 * 1) = 6 + 2 = 8

    The logic derived from the assertions is 2 * (radius + height).
    """
    return 2 * (radius + height)