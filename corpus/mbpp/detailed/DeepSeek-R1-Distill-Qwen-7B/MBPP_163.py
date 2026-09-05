import math

def area_polygon(n, s):
    """
    Calculate the area of a regular polygon with n sides each of length s.

    Parameters:
    n (int): Number of sides. Must be >=3.
    s (float): Length of each side. Must be >0.

    Returns:
    float: The area of the polygon with high precision.

    Raises:
    ValueError: If n is less than 3 or s is non-positive.
    """
    if not isinstance(n, int) or n < 3:
        raise ValueError("Number of sides must be an integer >= 3")
    if s <= 0:
        raise ValueError("Side length must be positive")

    pi = math.pi
    tan_val = math.tan(pi / n)
    area = (n * s ** 2) / (4 * tan_val)

    return area

# Test the function with the provided assertions
assert abs(area_polygon(4, 20) - 400.00000000000006) < 1e-10
assert abs(area_polygon(10, 15) - 1731.1969896610804) < 1e-10
assert abs(area_polygon(9, 7) - 302.90938549487214) < 1e-10