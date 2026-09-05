import math
from typing import Union

def validate_radius(radius_value: Union[int, float]) -> float:
    """
    Validates that the input is a numeric type (int or float) and represents
    a non-negative value suitable for a geometric radius.

    Args:
        radius_value: The potential radius value.

    Returns:
        The validated radius as a float.

    Raises:
        TypeError: If the input is not an int or float.
        ValueError: If the input is negative or NaN (Not a Number).
    """
    if not isinstance(radius_value, (int, float)):
        raise TypeError(f"Expected an int or float, got {type(radius_value).__name__}")

    # Handle float infinity and NaN cases which are invalid for physical dimensions
    if isinstance(radius_value, float):
        if math.isnan(radius_value):
            raise ValueError("Radius cannot be NaN (Not a Number)")
        if math.isinf(radius_value):
            raise ValueError("Radius cannot be infinite")

    if radius_value < 0:
        raise ValueError("Radius cannot be negative")

    return float(radius_value)

def calculate_surface_area_of_sphere(radius: float) -> float:
    """
    Calculates the surface area of a sphere given its radius.

    Formula: Surface Area = 4 * pi * r^2

    Args:
        radius: The radius of the sphere (must be non-negative).

    Returns:
        The surface area of the sphere.

    Raises:
        ValueError: If the radius is negative (should be caught by validate_radius).
    """
    # Define the constant PI using the math module for precision
    pi_value = math.pi

    # Calculate the square of the radius explicitly for clarity
    radius_squared = radius * radius

    # Calculate the final area using the formula: 4 * pi * r^2
    surface_area = 4 * pi_value * radius_squared

    return surface_area

def surfacearea_sphere(radius: Union[int, float]) -> float:
    """
    Main entry point to calculate the surface area of a sphere.

    This function performs input validation and delegates the calculation
    to the helper function. It handles edge cases such as zero radius,
    single element inputs (though a sphere doesn't have 'elements'),
    and invalid data types or negative values.

    Args:
        radius: The radius of the sphere.

    Returns:
        The surface area of the sphere as a float.

    Raises:
        TypeError: If radius is not a number.
        ValueError: If radius is negative or NaN.
    """
    # Step 1: Validate the input radius
    # This handles empty input logic implicitly (since no empty value is valid for a scalar)
    # It explicitly checks for negative numbers, zero (valid for degenerate sphere),
    # non-numeric types, and infinity.
    validated_radius = validate_radius(radius)

    # Step 2: Calculate the surface area
    # The calculation logic is isolated in the helper function
    calculated_area = calculate_surface_area_of_sphere(validated_radius)

    return calculated_area