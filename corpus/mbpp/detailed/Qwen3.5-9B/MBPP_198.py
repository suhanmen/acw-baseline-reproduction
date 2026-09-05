from typing import Union
import math

def largest_triangle(a: float, b: float) -> float:
    """
    Calculate the area of the largest triangle that can be inscribed in an ellipse.

    Mathematical derivation:
    The largest triangle inscribed in an ellipse with semi-axes 'a' and 'b'
    corresponds to an equilateral triangle scaled by the ellipse transformation.

    The area of an equilateral triangle inscribed in a unit circle (radius 1) is:
    Area_unit_circle = (3 * sqrt(3)) / 4

    When we transform the circle to an ellipse (scaling x by 'a' and y by 'b'),
    the area scales by the factor (a * b).

    Therefore: Area_ellipse = (3 * sqrt(3) / 4) * a * b

    Parameters:
    a (float): The length of the semi-major axis (must be positive)
    b (float): The length of the semi-minor axis (must be positive)

    Returns:
    float: The area of the largest inscribed triangle

    Raises:
    TypeError: If inputs are not numbers
    ValueError: If inputs are not positive (axes must be > 0)
    """

    # Step 1: Validate input types explicitly
    # Check if 'a' is a number
    if not isinstance(a, (int, float)):
        raise TypeError(f"Parameter 'a' must be a number, got {type(a).__name__}")

    # Check if 'b' is a number
    if not isinstance(b, (int, float)):
        raise TypeError(f"Parameter 'b' must be a number, got {type(b).__name__}")

    # Step 2: Validate input values (geometry constraints)
    # Semi-axes must be strictly positive for a valid ellipse
    if a <= 0.0:
        raise ValueError(f"Parameter 'a' must be strictly positive, got {a}")

    if b <= 0.0:
        raise ValueError(f"Parameter 'b' must be strictly positive, got {b}")

    # Step 3: Define mathematical constants with explicit names for clarity
    # The formula involves the constant: (3 * sqrt(3)) / 4
    sqrt_three = math.sqrt(3.0)
    equilateral_triangle_factor = (3.0 * sqrt_three) / 4.0

    # Step 4: Calculate the area of the corresponding equilateral triangle in a unit circle
    # This is the base area before scaling by the ellipse dimensions
    area_unit_circle_triangle = equilateral_triangle_factor

    # Step 5: Calculate the scaling factor for the area transformation
    # When transforming a circle to an ellipse, area scales by the product of the axes
    area_scaling_factor = a * b

    # Step 6: Compute the final result
    # Final Area = Base Area * Scaling Factor
    largest_triangle_area = area_unit_circle_triangle * area_scaling_factor

    return largest_triangle_area