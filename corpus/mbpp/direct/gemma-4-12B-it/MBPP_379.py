def surfacearea_cuboid(l: int, w: int, h: int) -> int:
    """
    Calculates the surface area of a cuboid given its length, width, and height.
    The formula for surface area is 2 * (lw + lh + wh).
    """
    return 2 * (l * w + l * h + w * h)