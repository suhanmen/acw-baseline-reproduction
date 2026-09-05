def lateralsurface_cuboid(length: float, width: float, height: float) -> float:
    """
    Calculate the lateral surface area of a cuboid.
    The lateral surface area is the area of all faces except the top and bottom.
    Formula: 2 * height * (length + width)
    """
    return 2 * height * (length + width)

if __name__ == "__main__":
    assert lateralsurface_cuboid(8, 5, 6) == 156
    assert lateralsurface_cuboid(7, 9, 10) == 320
    assert lateralsurface_cuboid(10, 20, 30) == 1800