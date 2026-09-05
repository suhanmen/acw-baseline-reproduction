def lateralsurface_cube(side_length):
    """
    Calculate the lateral surface area of a cube.

    Args:
        side_length (int): The length of one side of the cube. Must be a non-negative integer.

    Returns:
        int: The lateral surface area of the cube.

    Raises:
        ValueError: If side_length is not a non-negative integer.
    """
    # Input validation
    if not isinstance(side_length, int):
        raise ValueError("side_length must be an integer.")
    if side_length < 0:
        raise ValueError("side_length must be non-negative.")

    # Calculate lateral surface area
    lateral_area = 4 * (side_length ** 2)

    return lateral_area