def volume_cuboid(length: float, width: float, height: float) -> float:
    """
    Calculates the volume of a cuboid given its length, width, and height.
    """
    return float(length * width * height)

if __name__ == "__main__":
    assert volume_cuboid(1, 2, 3) == 6
    assert volume_cuboid(5, 7, 9) == 315
    assert volume_cuboid(10, 15, 21) == 3150