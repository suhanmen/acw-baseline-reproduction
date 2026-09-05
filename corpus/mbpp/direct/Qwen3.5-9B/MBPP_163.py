import math

def area_polygon(n, s):
    """
    Calculate the area of a regular polygon.

    Parameters:
    n (int): Number of sides
    s (float): Length of each side

    Returns:
    float: Area of the regular polygon
    """
    return (n * s ** 2) / (4 * math.tan(math.pi / n))