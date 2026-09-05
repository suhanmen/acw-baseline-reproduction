def surfacearea_cube(edge_length):
    """
    Calculate the surface area of a cube given the edge length.

    Args:
        edge_length (float|int): The length of an edge of the cube. Must be a positive number.

    Returns:
        float: The surface area of the cube.

    Raises:
        ValueError: If edge_length is zero or negative.
    """
    if not isinstance(edge_length, (int, float)) or edge_length <= 0:
        raise ValueError("Edge length must be a positive number.")

    surface_area = 6 * (edge_length ** 2)
    return surface_area

# Test cases
assert surfacearea_cube(5) == 150
assert surfacearea_cube(3) == 54
assert surfacearea_cube(10) == 600