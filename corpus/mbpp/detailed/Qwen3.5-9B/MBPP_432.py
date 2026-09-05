def _validate_inputs(top_base: float, bottom_base: float, height: float) -> None:
    """
    Validates that all input arguments are numeric and non-zero where required.

    Raises:
        TypeError: If any argument is not an int or float.
        ValueError: If any argument is zero, as a trapezium cannot have a dimension of zero.
    """
    # Check for correct types
    if not isinstance(top_base, (int, float)):
        raise TypeError(f"top_base must be a number, got {type(top_base).__name__}")
    if not isinstance(bottom_base, (int, float)):
        raise TypeError(f"bottom_base must be a number, got {type(bottom_base).__name__}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"height must be a number, got {type(height).__name__}")

    # Check for zero values
    if top_base == 0:
        raise ValueError("top_base cannot be zero")
    if bottom_base == 0:
        raise ValueError("bottom_base cannot be zero")
    if height == 0:
        raise ValueError("height cannot be zero")


def _calculate_area_and_height_squared(
    top_base: float,
    bottom_base: float,
    height: float
) -> tuple[float, float]:
    """
    Calculates the area of the trapezium and the square of the height.

    Returns:
        A tuple containing:
            - The area of the trapezium.
            - The square of the height.
    """
    sum_of_bases = top_base + bottom_base
    area = (sum_of_bases * height) / 2.0
    height_squared = height * height
    return area, height_squared


def _calculate_hypotenuse_squared_from_area_and_bases(
    area: float,
    top_base: float,
    bottom_base: float
) -> float:
    """
    Calculates the sum of the squares of the legs (hypotenuses) derived from
    the area, bases, and the geometric property of trapezoids.

    This uses the formula derived from the relationship between area, bases,
    height, and the sum of squared leg lengths.

    Formula used:
        Area = ( (b1 + b2) * h ) / 2
        Also relates to the 'median' m = (b1 + b2) / 2.
        The 'median' in this specific context (based on the problem examples)
        is calculated as the square root of (Area / height).
        However, looking at the examples:
        15, 25, 35 -> 20. ((15+25)/2 = 20). This is the standard arithmetic mean.
        10, 20, 30 -> 15. ((10+20)/2 = 15).
        6, 9, 4 -> 7.5. ((6+9)/2 = 7.5).

        Wait, the problem asks for "median of a trapezium".
        Standard definition of median of a trapezium is m = (b1 + b2) / 2.
        The third argument 'height' is unused in the standard formula?
        Let's re-examine the examples.

        Example 1: top=15, bottom=25, height=35. Result=20. (15+25)/2 = 20.
        Example 2: top=10, bottom=20, height=30. Result=15. (10+20)/2 = 15.
        Example 3: top=6, bottom=9, height=4. Result=7.5. (6+9)/2 = 7.5.

        In all cases, the result is simply (top_base + bottom_base) / 2.
        The 'height' parameter appears to be irrelevant for the calculation of the 
        arithmetic mean (median) of the bases, despite being part of the trapezium definition.

        Therefore, the calculation is strictly: (top_base + bottom_base) / 2.
        The validation still applies to ensure the object is a valid trapezium (non-zero dims).
    """
    # Re-evaluating the logic based on the explicit examples provided.
    # The examples clearly show: (a + b) / 2 = c.
    # The height variable is a distractor or strictly for validation.
    # We do not need the area or hypotenuse logic for the final answer,
    # but we will keep the validation step.
    return 0.0  # This function's return value is not used in the final calculation, 
               # keeping it here for structural clarity if expanded later, 
               # but the actual logic is below in _calculate_median.


def _calculate_median(
    top_base: float,
    bottom_base: float
) -> float:
    """
    Calculates the median of the trapezium using the arithmetic mean of the two bases.

    The median of a trapezium is defined as the line segment connecting the midpoints 
    of the non-parallel sides, and its length is the average of the lengths of the two parallel sides (bases).

    Formula:
        median = (top_base + bottom_base) / 2
    """
    sum_of_bases = top_base + bottom_base
    median_value = sum_of_bases / 2.0
    return median_value


def median_trapezium(top_base: float, bottom_base: float, height: float) -> float:
    """
    Calculates the median length of a trapezium given the lengths of its parallel bases and its height.

    The median of a trapezium is the length of the line segment connecting the midpoints of the two non-parallel sides.
    Mathematically, it is the arithmetic mean of the lengths of the two parallel bases.

    Note on inputs:
    - 'top_base' and 'bottom_base' are the lengths of the parallel sides.
    - 'height' is the perpendicular distance between the bases. While not used in the median formula itself,
      it is required to define the trapezium and is validated to ensure the shape is non-degenerate.

    Args:
        top_base: The length of the top parallel side.
        bottom_base: The length of the bottom parallel side.
        height: The height of the trapezium.

    Returns:
        The length of the median of the trapezium as a float.

    Raises:
        TypeError: If any input is not a number (int or float).
        ValueError: If any input is zero, which would make the trapezium degenerate.
    """
    _validate_inputs(top_base, bottom_base, height)

    sum_of_bases = top_base + bottom_base
    median_value = sum_of_bases / 2.0

    return median_value