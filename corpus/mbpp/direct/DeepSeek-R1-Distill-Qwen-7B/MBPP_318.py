def max_volume(s):
    """
    Find the maximum volume of a cuboid with given sum of sides.

    Args:
        s (int): The sum of all sides of the cuboid.

    Returns:
        int: The maximum volume of the cuboid if possible, otherwise 0.
    """
    if s % 3 != 0 or s < 3:
        return 0
    a = b = c = s // 3
    return a * b * c