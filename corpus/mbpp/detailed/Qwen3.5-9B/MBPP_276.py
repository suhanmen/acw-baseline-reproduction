import math
from typing import Tuple, Union

Number = Union[int, float]

def _validate_radius(radius: Number) -> Number:
    """
    Validates that the radius is a numeric type and is non-negative.

    Parameters:
    radius (Number): The value to validate as a radius.

    Returns:
    Number: The validated radius value.

    Raises:
    TypeError: If the radius is not an int or float.
    ValueError: If the radius is negative.
    """
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a number (int or float), got {type(radius).__name__}.")

    if math.isnan(radius):
        raise ValueError("Radius cannot be NaN (Not a Number).")

    if math.isinf(radius):
        raise ValueError("Radius cannot be infinite.")

    if radius < 0:
        raise ValueError("Radius must be non-negative.")

    return radius


def _validate_height(height: Number) -> Number:
    """
    Validates that the height is a numeric type. Height can be zero or negative 
    for pure mathematical volume calculation, though physically height is often positive.
    This implementation allows zero and negative heights but validates the type.

    Parameters:
    height (Number): The value to validate as a height.

    Returns:
    Number: The validated height value.

    Raises:
    TypeError: If the height is not an int or float.
    """
    if not isinstance(height, (int, float)):
        raise TypeError(f"Height must be a number (int or float), got {type(height).__name__}.")

    if math.isnan(height):
        raise ValueError("Height cannot be NaN (Not a Number).")

    if math.isinf(height):
        raise ValueError("Height cannot be infinite.")

    return height


def _calculate_base_area(radius: Number) -> float:
    """
    Calculates the area of the circular base of the cylinder.

    Formula: Area = π * r^2

    Parameters:
    radius (Number): The radius of the base.

    Returns:
    float: The calculated base area.
    """
    return math.pi * (radius ** 2)


def _calculate_volume(base_area: float, height: Number) -> float:
    """
    Calculates the volume of the cylinder given the base area and height.

    Formula: Volume = Base Area * Height

    Parameters:
    base_area (float): The area of the circular base.
    height (Number): The height of the cylinder.

    Returns:
    float: The calculated volume.
    """
    return base_area * height


def volume_cylinder(radius: Number, height: Number) -> float:
    """
    Calculates the volume of a cylinder given its radius and height.

    This function performs rigorous input validation before performing the calculation.
    It handles edge cases such as zero radius, zero height, and negative values
    by either returning a mathematically correct result (often 0) or raising 
    specific exceptions where a value is physically or logically impossible.

    Parameters:
    radius (Number): The radius of the cylinder's base. Must be non-negative.
    height (Number): The height of the cylinder. Can be any number.

    Returns:
    float: The volume of the cylinder.

    Raises:
    TypeError: If radius or height are not numeric types.
    ValueError: If radius is negative, NaN, or infinite.
    """
    # Step 1: Validate the radius argument
    validated_radius = _validate_radius(radius)

    # Step 2: Validate the height argument
    validated_height = _validate_height(height)

    # Step 3: Calculate the area of the circular base
    base_area = _calculate_base_area(validated_radius)

    # Step 4: Calculate the final volume
    final_volume = _calculate_volume(base_area, validated_height)

    # Step 5: Handle specific degenerate cases logically before return
    # If radius is zero, volume is zero regardless of height
    # If height is zero, volume is zero regardless of radius
    if validated_radius == 0 or validated_height == 0:
        return 0.0

    return final_volume