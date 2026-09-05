import math
from typing import Union

Number = Union[int, float]

def _validate_radius_and_height(
    radius: Number,
    height: Number,
) -> None:
    """
    Validate that the provided radius and height are valid numbers
    and satisfy the geometric constraints of a cone:
    - Must be numeric (int or float).
    - Must be non-negative (>= 0).
    - If negative or NaN, raise a ValueError.

    This function explicitly checks for type correctness, range validity,
    and degeneracy (negative or NaN values).
    """

    # Check for type validity explicitly
    if not isinstance(radius, (int, float)):
        raise TypeError(f"Radius must be a number, got {type(radius).__name__}")
    if not isinstance(height, (int, float)):
        raise TypeError(f"Height must be a number, got {type(height).__name__}")

    # Convert to float to handle both int and float uniformly for further checks
    radius_float = float(radius)
    height_float = float(height)

    # Check for NaN explicitly using math.isnan
    if math.isnan(radius_float):
        raise ValueError("Radius cannot be NaN")
    if math.isnan(height_float):
        raise ValueError("Height cannot be NaN")

    # Check for negative values explicitly
    if radius_float < 0:
        raise ValueError(f"Radius cannot be negative, got {radius_float}")
    if height_float < 0:
        raise ValueError(f"Height cannot be negative, got {height_float}")

def _compute_cone_volume(radius: Number, height: Number) -> float:
    """
    Compute the volume of a cone using the standard formula:
        V = (1/3) * π * r^2 * h

    Parameters:
        radius (Number): The radius of the base of the cone.
        height (Number): The height of the cone.

    Returns:
        float: The calculated volume of the cone.
    """

    # Use the validated radius directly (no re-validation needed if caller trusts _validate_radius_and_height)
    # However, for robustness within this specific helper, we cast to float to ensure consistency.
    current_radius = float(radius)

    # Calculate the square of the radius explicitly
    squared_radius = current_radius * current_radius

    # Retrieve the constant Pi from the math module
    pi_value = math.pi

    # Calculate the base area: A = π * r^2
    base_area = pi_value * squared_radius

    # Calculate the volume: V = (1/3) * base_area * height
    # We use explicit multiplication and division to show the steps clearly.
    third_of_height = height / 3.0
    volume = base_area * third_of_height

    return volume

def volume_cone(radius: Number, height: Number) -> float:
    """
    Calculate the volume of a cone given its radius and height.

    The formula used is: V = (1/3) * π * r^2 * h

    Parameters:
        radius (Number): The radius of the cone's base. Must be non-negative.
        height (Number): The perpendicular height of the cone. Must be non-negative.

    Returns:
        float: The volume of the cone.

    Raises:
        TypeError: If radius or height is not a numeric type.
        ValueError: If radius or height is negative or NaN.
    """

    # Step 1: Validate inputs explicitly
    _validate_radius_and_height(radius, height)

    # Step 2: Compute the volume using the helper function
    # This separation ensures logic is isolated and testable.
    result_volume = _compute_cone_volume(radius, height)

    # Return the computed volume
    return result_volume