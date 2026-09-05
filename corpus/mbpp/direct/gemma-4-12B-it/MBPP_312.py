import math

def volume_cone(radius, height):
    """
    Calculates the volume of a cone given its radius and height.
    Formula: V = (1/3) * pi * r^2 * h
    """
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume