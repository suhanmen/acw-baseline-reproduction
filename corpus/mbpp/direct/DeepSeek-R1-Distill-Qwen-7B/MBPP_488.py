import math

def area_pentagon(sides):
    if sides < 3:
        raise ValueError("A pentagon must have exactly 5 sides.")

    # Formula for the area of a regular pentagon: (5/2) * s^2 * (1 / tan(pi/5))
    area = (5 / 2) * (sides ** 2) * (1 / math.tan(math.pi / 5))

    return area