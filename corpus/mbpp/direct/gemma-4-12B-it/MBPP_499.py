def diameter_circle(radius):
    """
    Calculates the diameter of a circle given its radius.

    Args:
        radius (float/int): The radius of the circle.

    Returns:
        float/int: The diameter of the circle.
    """
    return 2 * radius

if __name__ == "__main__":
    assert diameter_circle(10) == 20
    assert diameter_circle(40) == 80
    assert diameter_circle(15) == 30