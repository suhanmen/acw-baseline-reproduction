def surfacearea_cuboid(length, width, height):
    """
    Calculate the surface area of a cuboid.

    The surface area of a cuboid is calculated using the formula:
    2 * (length * width + length * height + width * height)

    Args:
        length (int): The length of the cuboid.
        width (int): The width of the cuboid.
        height (int): The height of the cuboid.

    Returns:
        int: The surface area of the cuboid.
    """
    return 2 * (length * width + length * height + width * height)