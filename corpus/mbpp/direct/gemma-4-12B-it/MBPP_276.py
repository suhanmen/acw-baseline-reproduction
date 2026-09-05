import math

def volume_cylinder(radius: float, height: float) -> float:
    """
    Calculate the volume of a cylinder given its radius and height.
    Formula: V = pi * r^2 * h
    """
    return math.pi * (radius ** 2) * height

if __name__ == "__main__":
    assert volume_cylinder(10, 5) == 1570.7500000000002
    assert volume_cylinder(4, 5) == 251.32000000000002
    assert volume_cylinder(4, 10) == 502.64000000000004