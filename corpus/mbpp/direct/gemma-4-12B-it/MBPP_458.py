def rectangle_area(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle given its length and width.
    """
    return float(length * width)

if __name__ == "__main__":
    assert rectangle_area(10, 20) == 200
    assert rectangle_area(10, 5) == 50
    assert rectangle_area(4, 2) == 8