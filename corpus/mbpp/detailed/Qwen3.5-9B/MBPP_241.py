def _validate_dimensions(x: int, y: int, z: int) -> None:
    """
    Validates that the input dimensions x, y, and z are positive integers.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any argument is not a positive integer (<= 0).
    """
    # Check for type correctness
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError(f"Dimension x must be an integer, got {type(x).__name__}")

    if not isinstance(y, int) or isinstance(y, bool):
        raise TypeError(f"Dimension y must be an integer, got {type(y).__name__}")

    if not isinstance(z, int) or isinstance(z, bool):
        raise TypeError(f"Dimension z must be an integer, got {type(z).__name__}")

    # Check for positivity (must be strictly greater than zero)
    if x <= 0:
        raise ValueError(f"Dimension x must be positive, got {x}")

    if y <= 0:
        raise ValueError(f"Dimension y must be positive, got {y}")

    if z <= 0:
        raise ValueError(f"Dimension z must be positive, got {z}")


def _create_row(width: int) -> list:
    """
    Creates a single 1D row list containing 'width' asterisk characters.

    Args:
        width: The number of columns in the row.

    Returns:
        A list of strings, where each string is '*'.
    """
    return ['*'] * width


def _create_plane(depth: int, row_content: list) -> list:
    """
    Creates a single 2D plane (list of rows) by replicating the row content.

    Args:
        depth: The number of rows in the plane.
        row_content: The list representing a single row (output of _create_row).

    Returns:
        A list of lists, representing a 2D plane.
    """
    plane = []
    for _ in range(depth):
        plane.append(row_content)
    return plane


def _create_block(height: int, plane_content: list) -> list:
    """
    Creates the final 3D block by stacking planes.

    Args:
        height: The number of planes (layers) in the block.
        plane_content: The list representing a single plane (output of _create_plane).

    Returns:
        A list of lists of lists, representing the 3D array.
    """
    block = []
    for _ in range(height):
        block.append(plane_content)
    return block


def array_3d(x: int, y: int, z: int) -> list:
    """
    Generates a 3D array (list of lists of lists) where every element is '*'.

    The dimensions correspond to:
    - x: The number of planes (layers) in the outermost list.
    - y: The number of rows in each plane.
    - z: The number of columns in each row.

    Args:
        x: The size of the first dimension (depth/height of the block).
        y: The size of the second dimension (rows per plane).
        z: The size of the third dimension (columns per row).

    Returns:
        A 3D list structure fully populated with '*' strings.

    Raises:
        TypeError: If inputs are not integers (excluding booleans).
        ValueError: If any input is not a positive integer.
    """
    # Step 1: Validate inputs strictly before proceeding with generation
    _validate_dimensions(x, y, z)

    # Step 2: Create a single representative row based on dimension z
    single_row = _create_row(z)

    # Step 3: Create a single representative plane by repeating the row y times
    single_plane = _create_plane(y, single_row)

    # Step 4: Create the final 3D block by repeating the plane x times
    final_block = _create_block(x, single_plane)

    return final_block