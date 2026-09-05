def surfacearea_cube(side_length: int) -> int:
    """
    Calculate the surface area of a cube given the length of one side.

    The surface area of a cube is calculated as 6 * (side_length ** 2),
    since a cube has 6 identical square faces.

    Args:
        side_length (int): The length of one side of the cube.

    Returns:
        int: The total surface area of the cube.

    Raises:
        TypeError: If side_length is not an integer.
        ValueError: If side_length is negative.

    Examples:
        >>> surfacearea_cube(5)
        150
        >>> surfacearea_cube(3)
        54
        >>> surfacearea_cube(10)
        600
    """

    # Validate the type of the input
    if not isinstance(side_length, int):
        raise TypeError(f"Expected integer input for side_length, but got {type(side_length).__name__}")

    # Validate the value of the input (side length must be non-negative)
    if side_length < 0:
        raise ValueError(f"Side length cannot be negative. Received: {side_length}")

    # Handle the degenerate case of zero explicitly (a cube with side 0 has 0 surface area)
    if side_length == 0:
        return 0

    # Calculate the area of one square face
    face_area = side_length * side_length

    # A cube has exactly 6 faces
    number_of_faces = 6

    # Calculate the total surface area
    total_surface_area = number_of_faces * face_area

    return total_surface_area