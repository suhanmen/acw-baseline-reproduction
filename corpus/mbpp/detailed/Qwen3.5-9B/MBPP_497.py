import math
from typing import Union

def _validate_radius(radius: Union[int, float]) -> None:
    """
    Validates that the radius is a finite, non-negative number.

    Args:
        radius: The radius value to validate.

    Raises:
        TypeError: If radius is not a number (int or float).
        ValueError: If radius is negative or not finite (e.g., NaN or Inf).
    """
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a numeric type (int or float), got {type(radius).__name__}")

    # Check for negative numbers
    if radius < 0:
        raise ValueError(f"Radius cannot be negative, got {radius}")

    # Check for NaN (Not a Number)
    if math.isnan(radius):
        raise ValueError(f"Radius cannot be NaN, got {radius}")

    # Check for Infinity
    if math.isinf(radius):
        raise ValueError(f"Radius cannot be infinite, got {radius}")

def _validate_height(height: Union[int, float]) -> None:
    """
    Validates that the height is a finite, non-negative number.

    Args:
        height: The height value to validate.

    Raises:
        TypeError: If height is not a number (int or float).
        ValueError: If height is negative or not finite (e.g., NaN or Inf).
    """
    if not isinstance(height, (int, float)):
        raise TypeError(f"Height must be a numeric type (int or float), got {type(height).__name__}")

    if height < 0:
        raise ValueError(f"Height cannot be negative, got {height}")

    if math.isnan(height):
        raise ValueError(f"Height cannot be NaN, got {height}")

    if math.isinf(height):
        raise ValueError(f"Height cannot be infinite, got {height}")

def _calculate_slant_height(radius: float, height: float) -> float:
    """
    Calculates the slant height of the cone using the Pythagorean theorem.
    slant_height = sqrt(radius^2 + height^2)

    Args:
        radius: The radius of the base.
        height: The perpendicular height of the cone.

    Returns:
        The slant height as a float.
    """
    radius_squared = radius * radius
    height_squared = height * height
    sum_of_squares = radius_squared + height_squared
    slant_height = math.sqrt(sum_of_squares)
    return slant_height

def _calculate_base_area(radius: float) -> float:
    """
    Calculates the area of the circular base of the cone.
    base_area = pi * radius^2

    Args:
        radius: The radius of the base.

    Returns:
        The base area as a float.
    """
    radius_squared = radius * radius
    base_area = math.pi * radius_squared
    return base_area

def _calculate_lateral_surface_area(radius: float, slant_height: float) -> float:
    """
    Calculates the lateral (side) surface area of the cone.
    lateral_area = pi * radius * slant_height

    Args:
        radius: The radius of the base.
        slant_height: The slant height of the cone.

    Returns:
        The lateral surface area as a float.
    """
    lateral_surface_area = math.pi * radius * slant_height
    return lateral_surface_area

def surfacearea_cone(radius: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculates the total surface area of a cone.

    The total surface area is the sum of the base area and the lateral surface area.
    Formula: Total Area = (pi * radius^2) + (pi * radius * slant_height)
    Where slant_height = sqrt(radius^2 + height^2)

    Args:
        radius: The radius of the cone's base. Must be non-negative.
        height: The perpendicular height of the cone. Must be non-negative.

    Returns:
        The total surface area as a float.

    Raises:
        TypeError: If radius or height are not numeric.
        ValueError: If radius or height are negative, NaN, or infinite.
    """
    # Step 1: Validate inputs
    _validate_radius(radius)
    _validate_height(height)

    # Step 2: Handle edge case where both radius and height are zero
    # In this degenerate case, the cone has no volume and no surface area (mathematically 0).
    if radius == 0 and height == 0:
        return 0.0

    # Step 3: Calculate intermediate geometric properties
    slant_height = _calculate_slant_height(radius, height)
    base_area = _calculate_base_area(radius)
    lateral_surface_area = _calculate_lateral_surface_area(radius, slant_height)

    # Step 4: Sum the components to get the total surface area
    total_surface_area = base_area + lateral_surface_area

    return total_surface_area