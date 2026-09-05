import math
from typing import Union

def _validate_positive_dimensions(r: float, h: float) -> None:
    """
    Validates that the radius (r) and height (h) are strictly positive numbers.

    Raises:
        ValueError: If either dimension is not a number, is not finite, 
                    or is less than or equal to zero.
    """
    # Check if inputs are numbers
    if not isinstance(r, (int, float)):
        raise TypeError(f"Radius must be a number, got {type(r).__name__}")
    if not isinstance(h, (int, float)):
        raise TypeError(f"Height must be a number, got {type(h).__name__}")

    # Check for NaN
    if math.isnan(r):
        raise ValueError("Radius cannot be NaN (Not a Number)")
    if math.isnan(h):
        raise ValueError("Height cannot be NaN (Not a Number)")

    # Check for Infinity
    if math.isinf(r):
        raise ValueError("Radius cannot be infinity")
    if math.isinf(h):
        raise ValueError("Height cannot be infinity")

    # Check for non-positive values (cylinder dimensions must be > 0)
    if r <= 0:
        raise ValueError(f"Radius must be strictly positive, got {r}")
    if h <= 0:
        raise ValueError(f"Height must be strictly positive, got {h}")


def _calculate_circumference(r: float) -> float:
    """
    Calculates the circumference of the circular base of the cylinder.

    Formula: C = 2 * pi * r

    Args:
        r (float): The radius of the cylinder's base.

    Returns:
        float: The circumference.
    """
    return 2.0 * math.pi * r


def _calculate_lateral_surface_height(h: float) -> float:
    """
    Prepares the height component for the perimeter calculation.

    In the context of the provided test cases (e.g., perimeter(2,4)==12),
    the "perimeter" requested by the problem is not the standard geometric
    total surface area or circumference alone. The test cases imply a 
    specific linear dimension definition often found in simplified physics 
    or specific engineering contexts for "perimeter" involving these two inputs.

    However, looking strictly at the provided assertions:
    - perimeter(2, 4) == 12  => 2 + 4 + 2 + 4? Or 2*(2+4)?
    - perimeter(1, 2) == 6  => 1 + 2 + 1 + 2? Or 2*(1+2)?
    - perimeter(3, 1) == 8  => 3 + 1 + 3 + 1? Or 2*(3+1)?

    The pattern matches 2 * (r + h) = 2r + 2h.

    Note: Standard geometry defines "perimeter" for a 3D object as non-standard 
    or refers to the perimeter of the base (2*pi*r) or cross section. 
    Given the explicit integer arithmetic in the assertions, this function 
    implements the logic required to satisfy the provided test cases exactly.

    Args:
        h (float): The height of the cylinder.

    Returns:
        float: The total linear contribution of the height to the specific 
               definition of "perimeter" required by the problem (2 * h).
    """
    return 2.0 * h


def _calculate_lateral_surface_radius_contribution(r: float) -> float:
    """
    Prepares the radius component for the perimeter calculation.

    Based on the pattern identified in _calculate_lateral_surface_height,
    this returns 2 * r.

    Args:
        r (float): The radius of the cylinder's base.

    Returns:
        float: The total linear contribution of the radius (2 * r).
    """
    return 2.0 * r


def perimeter(radius: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculates the specific "perimeter" value defined by the problem constraints.

    Based on the provided assertions, the function calculates: 2 * (radius + height).
    This differs from standard geometric definitions of cylinder perimeter (which 
    usually refers to the base circumference) but satisfies the explicit unit tests.

    Args:
        radius (Union[int, float]): The radius of the cylinder base.
        height (Union[int, float]): The height of the cylinder.

    Returns:
        float: The calculated perimeter value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive or are not finite.
    """
    # Step 1: Validate inputs explicitly
    _validate_positive_dimensions(radius, height)

    # Step 2: Calculate the radius component (2 * radius)
    radius_component = _calculate_lateral_surface_radius_contribution(radius)

    # Step 3: Calculate the height component (2 * height)
    height_component = _calculate_lateral_surface_height(height)

    # Step 4: Sum the components to get the final result
    final_perimeter = radius_component + height_component

    return final_perimeter