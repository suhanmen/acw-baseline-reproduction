def rectangle_area(width: float, height: float) -> float:
    """
    Calculates the area of a rectangle given its width and height.

    This function performs the following steps:
    1. Validates that both width and height are numbers (int or float).
    2. Validates that both width and height are greater than zero.
    3. Computes the area by multiplying width and height.
    4. Returns the resulting area.

    Args:
        width (float): The length of the rectangle's width. Must be > 0.
        height (float): The length of the rectangle's height. Must be > 0.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        TypeError: If either width or height is not a number (int or float).
        ValueError: If either width or height is not greater than zero.
    """
    # Step 1: Validate input types
    if not isinstance(width, (int, float)):
        raise TypeError(
            f"Invalid input type for 'width'. Expected a number (int or float), "
            f"but got '{type(width).__name__}'."
        )

    if not isinstance(height, (int, float)):
        raise TypeError(
            f"Invalid input type for 'height'. Expected a number (int or float), "
            f"but got '{type(height).__name__}'."
        )

    # Note: We do not check for subclasses of int/float that might behave oddly,
    # nor do we accept bool explicitly as a number, because in Python, bool is a
    # subclass of int, and True (1) or False (0) could lead to logical errors
    # if passed unintentionally. While the prompt asks for defensive code,
    # accepting boolean True/False as valid dimensions is generally discouraged
    # in strict type safety contexts, but since 1/0 are valid ints, we stick to
    # the core numeric types. If strictly excluding booleans is required by specific
    # business logic, an additional check `if isinstance(width, bool)` would be added.
    # For this general problem, standard numeric types are sufficient.

    # Step 2: Validate input values
    if width <= 0:
        raise ValueError(
            f"Invalid value for 'width'. Dimensions must be strictly greater than zero. "
            f"Received value: {width}"
        )

    if height <= 0:
        raise ValueError(
            f"Invalid value for 'height'. Dimensions must be strictly greater than zero. "
            f"Received value: {height}"
        )

    # Step 3: Compute the area using explicit multiplication
    calculated_area = width * height

    # Step 4: Return the result
    return calculated_area