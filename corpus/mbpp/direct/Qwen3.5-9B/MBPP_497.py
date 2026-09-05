import math

def surfacearea_cone(r, h):
    """
    Calculate the surface area of a cone.

    Parameters:
    r (float): Radius of the base of the cone.
    h (float): Height of the cone.

    Returns:
    float: Surface area of the cone.
    """
    l = math.sqrt(r**2 + h**2)
    base_area = math.pi * r**2
    lateral_area = math.pi * r * l
    return base_area + lateral_area