def surfacearea_cuboid(length: float, width: float, height: float) -> float:
    """
    Calculate the total surface area of a cuboid.

    The surface area A of a cuboid with dimensions l, w, h is given by:
    A = 2 * (l*w + w*h + h*l)

    Parameters
    ----------
    length : float
        The length of the cuboid.
    width : float
        The width of the cuboid.
    height : float
        The height of the cuboid.

    Returns
    -------
    float
        The total surface area of the cuboid.

    Raises
    ------
    TypeError
        If any of the inputs are not numeric types.
    ValueError
        If any of the dimensions are negative (a cuboid cannot have negative dimensions).
        If all dimensions are zero (a cuboid with no volume/area is degenerate).
    """

    # Step 1: Validate input types explicitly
    if not isinstance(length, (int, float)):
        raise TypeError(f"Expected numeric type for 'length', got {type(length).__name__}")
    if not isinstance(width, (int, float)):
        raise TypeError(f"Expected numeric type for 'width', got {type(width).__name__}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"Expected numeric type for 'height', got {type(height).__name__})

    # Step 2: Validate dimension values for negativity
    # A cuboid with negative dimensions is physically impossible in this context
    if length < 0:
        raise ValueError(f"Dimension 'length' cannot be negative. Provided: {length}")
    if width < 0:
        raise ValueError(f"Dimension 'width' cannot be negative. Provided: {width}")
    if height < 0:
        raise ValueError(f"Dimension 'height' cannot be negative. Provided: {height}")

    # Step 3: Handle the degenerate case where all dimensions are zero
    # A cuboid with all zero dimensions has no surface area, but this is a degenerate input.
    # We choose to raise an error for zero dimensions as per defensive programming principles
    # unless the problem specifically requests returning 0.0 for this case.
    # Given the context of "surface area of a cuboid", a zero-size object is invalid input.
    if length == 0 and width == 0 and height == 0:
        raise ValueError("All dimensions cannot be zero simultaneously.")

    # Step 4: Validate that at least one dimension is non-zero to ensure it's a valid geometric entity
    # If two are zero and one is non-zero, the "surface area" is just the area of two faces,
    # which mathematically works, but often implies a line or point depending on context.
    # However, the formula 2*(lw + wh + hl) handles these cases naturally (result would be 0 if two are 0).
    # The only strict failure is negative numbers or all zeros.

    # Step 5: Calculate the area of the three distinct faces explicitly
    # Face 1: Length x Width
    area_length_width = length * width

    # Face 2: Width x Height
    area_width_height = width * height

    # Face 3: Height x Length
    area_height_length = height * length

    # Step 6: Sum the areas of the three faces
    sum_of_face_areas = area_length_width + area_width_height + area_height_length

    # Step 7: Multiply by 2 to get the total surface area (since every face has an opposite)
    total_surface_area = 2.0 * sum_of_face_areas

    # Return the calculated surface area
    return total_surface_area