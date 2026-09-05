def array_3d(rows, cols, depth=1):
    """
    Generates a 3D array filled with '*' characters.

    Requirements:
    - rows: Number of elements along the first dimension.
    - cols: Number of elements along the second dimension.
    - depth: Number of elements along the third dimension (default is 1).

    Returns:
    A 3D list where each element is '*'.

    Raises:
    ValueError: If any of the dimensions are less than or equal to 0.
    """
    # Validate the input dimensions
    if rows <= 0 or cols <= 0 or depth <= 0:
        raise ValueError("All dimensions must be greater than 0.")

    # Create a 2D list filled with '*' for each layer
    def create_2d层(row, col):
        return [[ '*' for _ in range(col)] for _ in range(row)]

    # Create the 3D array by stacking the 2D layers
    result = []
    for _ in range(depth):
        result.append(create_2d层(rows, cols))

    return result