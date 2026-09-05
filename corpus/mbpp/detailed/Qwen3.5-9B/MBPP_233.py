import math
from typing import Tuple, Union

Number = Union[int, float]

def _validate_radius(radius: Number) -> None:
    """
    Validates that the radius is a numeric value greater than zero.
    Raises a ValueError if the input is invalid.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")

    if math.isnan(radius):
        raise ValueError("Radius cannot be NaN (Not a Number).")

    if math.isinf(radius):
        raise ValueError("Radius cannot be infinite.")

    if radius <= 0:
        raise ValueError(f"Radius must be strictly positive, got {radius}.")


def _validate_height(height: Number) -> None:
    """
    Validates that the height is a numeric value greater than zero.
    Raises a ValueError if the input is invalid.
    """
    if not isinstance(height, (int, float)):
        raise TypeError(f"Height must be a number, got {type(height).__name__}")

    if math.isnan(height):
        raise ValueError("Height cannot be NaN (Not a Number).")

    if math.isinf(height):
        raise ValueError("Height cannot be infinite.")

    if height <= 0:
        raise ValueError(f"Height must be strictly positive, got {height}.")


def _calculate_lateral_surface_area(radius: Number, height: Number) -> float:
    """
    Calculates the lateral surface area of a cylinder.

    Formula: Lateral Area = 2 * pi * r * h

    Parameters:
        radius: The radius of the cylinder base.
        height: The height of the cylinder.

    Returns:
        The calculated lateral surface area as a float.
    """
    # Define pi using the standard math module for precision
    pi_value: float = math.pi

    # Calculate the circumference of the base: 2 * pi * r
    circumference: float = 2.0 * pi_value * radius

    # Calculate the lateral surface area: circumference * height
    area: float = circumference * height

    return area


def lateralsuface_cylinder(radius: Number, height: Number) -> float:
    """
    Computes the lateral surface area of a cylinder given its radius and height.

    The lateral surface area is the area of the side surface of the cylinder,
    excluding the top and bottom circular bases.

    Args:
        radius (Number): The radius of the cylinder's base. Must be positive.
        height (Number): The height of the cylinder. Must be positive.

    Returns:
        float: The calculated lateral surface area.

    Raises:
        TypeError: If radius or height are not numeric.
        ValueError: If radius or height are non-positive, NaN, or infinite.

    Examples:
        >>> lateralsuface_cylinder(10, 5)
        314.15000000000003
        >>> lateralsuface_cylinder(4, 5)
        125.66000000000001
        >>> lateralsuface_cylinder(4, 10)
        251.32000000000002
    """
    # Step 1: Validate the radius input
    _validate_radius(radius)

    # Step 2: Validate the height input
    _validate_height(height)

    # Step 3: Calculate and return the lateral surface area
    return _calculate_lateral_surface_area(radius, height)