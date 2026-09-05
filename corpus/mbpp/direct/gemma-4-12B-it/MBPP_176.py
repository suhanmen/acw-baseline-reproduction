def perimeter_triangle(a: float, b: float, c: float) -> float:
    """
    Calculate the perimeter of a triangle given the lengths of its three sides.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        float: The sum of the lengths of the three sides.
    """
    return float(a + b + c)

if __name__ == "__main__":
    assert perimeter_triangle(10, 20, 30) == 60
    assert perimeter_triangle(3, 4, 5) == 12
    assert perimeter_triangle(25, 35, 45) == 105