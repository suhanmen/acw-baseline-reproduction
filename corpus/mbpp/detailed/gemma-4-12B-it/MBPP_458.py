import math

def rectangle_area(width: float, height: float) -> float:
    """
    Calculates the area of a rectangle given its width and height.

    The function validates that both inputs are numeric and non-negative,
    as a rectangle cannot have negative or zero dimensions in a physical
    context (or at least, its area would be zero/undefined in standard geometry).

    Args:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The calculated area of the rectangle.

    Raises:
        TypeError: If width or height are not int or float.
        ValueError: If width or height are negative numbers.
    """

    # Step 1: Validate that the inputs are of the correct types.
    # We accept both integers and floats as valid inputs.
    is_width_numeric = isinstance(width, (int, float))
    is_height_numeric = isinstance(height, (int, float))

    if not is_width_numeric or not is_height_numeric:
        raise TypeError(
            f"Inputs must be numeric. Received width: {type(width)}, height: {type(height)}"
        )

    # Step 2: Validate that the dimensions are non-negative.
    # A rectangle with a negative side length is geometrically undefined.
    if width < 0:
        raise ValueError(f"Width must be non-negative. Received: {width}")

    if height < 0:
        raise ValueError(f"Height must be non-negative. Received: {height}")

    # Step 3: Handle the edge case where dimensions are zero.
    # While technically a "degenerate" rectangle, the area should be 0.0.
    if width == 0 or height == 0:
        area = 0.0
        return float(area)

    # Step 4: Calculate the area.
    # Area = width * height
    calculated_area = float(width) * float(height)

    # Step 5: Return the result.
    return calculated_area

if __name__ == "__main__":
    # Testing the provided assertions
    assert rectangle_area(10, 20) == 200
    assert rectangle_area(10, 5) == 50
    assert rectangle_area(4, 2) == 8