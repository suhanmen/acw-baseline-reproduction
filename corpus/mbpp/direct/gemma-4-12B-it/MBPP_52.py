def parallelogram_area(base, height):
    """
    Calculates the area of a parallelogram given its base and height.

    Args:
        base (float): The length of the base of the parallelogram.
        height (float): The perpendicular height of the parallelogram.

    Returns:
        float: The area of the parallelogram.
    """
    return base * height

if __name__ == "__main__":
    assert parallelogram_area(10, 20) == 200
    assert parallelogram_area(15, 20) == 300
    assert parallelogram_area(8, 9) == 72