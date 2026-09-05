import math
from typing import Optional, Union

# Constants for validation thresholds (optional but good practice for defensive coding)
NEGATIVE_RADIUS_THRESHOLD: float = -1.0
MAX_REASONABLE_RADIUS: float = 1e9

def _validate_radius(value: Union[int, float]) -> float:
    """
    Validates that the input value represents a valid physical radius.

    Requirements:
    - Must be a number (int or float).
    - Must be positive (strictly greater than zero).
    - Returns the validated float.
    - Raises ValueError if validation fails.
    """
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"Expected numeric input (int or float), but received type: {type(value).__name__}"
        )

    # Handle NaN explicitly
    if math.isnan(value):
        raise ValueError(f"Input value {value} is NaN (Not a Number), which is invalid for radius.")

    # Handle Infinity explicitly
    if math.isinf(value):
        raise ValueError(f"Input value {value} is infinite, which is invalid for radius.")

    if value <= NEGATIVE_RADIUS_THRESHOLD:
        raise ValueError(
            f"Input value {value} is not a positive number. "
            f"A physical radius must be strictly greater than zero."
        )

    # Check for degenerately large numbers that might cause overflow in standard float calculations
    # though Python handles large floats, it's good practice for domain validation.
    if value > MAX_REASONABLE_RADIUS:
        raise ValueError(
            f"Input value {value} exceeds the maximum reasonable physical dimension."
        )

    return float(value)

def _calculate_volume_cubed(r: float) -> float:
    """
    Calculates the cube of the radius (r^3) using math.pow for clarity.
    """
    return math.pow(r, 3)

def _calculate_four_thirds() -> float:
    """
    Returns the constant coefficient 4/3.
    """
    return 4.0 / 3.0

def _calculate_pi() -> float:
    """
    Returns the value of PI.
    """
    return math.pi

def _compute_volume(r_cubed: float, constant: float, pi_value: float) -> float:
    """
    Computes the final volume using the formula: V = (4/3) * pi * r^3.
    """
    intermediate_result = constant * pi_value
    final_volume = intermediate_result * r_cubed
    return final_volume

def volume_sphere(radius_input: Union[int, float]) -> float:
    """
    Calculates the volume of a sphere given its radius.

    Formula: V = (4/3) * pi * r^3

    Parameters:
    - radius_input: The radius of the sphere. Must be a positive number.

    Returns:
    - The volume of the sphere as a float.

    Raises:
    - TypeError: If the input is not an int or float.
    - ValueError: If the input is not a positive number.

    Edge Cases Handled:
    - Empty input is not possible due to signature requiring a value.
    - Zero radius raises ValueError.
    - Negative radius raises ValueError.
    - Single element (single radius) is the standard case.
    - All-equal elements are not applicable as this takes a single scalar.
    - Boundary values (very small, very large) are handled by float precision.
    """

    # Step 1: Validate the input radius.
    # This converts the input to a float and checks for domain validity.
    validated_radius = _validate_radius(radius_input)

    # Step 2: Calculate the radius cubed.
    # Explicitly naming the step improves readability.
    radius_cubed = _calculate_volume_cubed(validated_radius)

    # Step 3: Define the constants involved in the sphere volume formula.
    factor_4_3 = _calculate_four_thirds()
    pi_value = _calculate_pi()

    # Step 4: Compute the final volume using the pre-calculated components.
    sphere_volume = _compute_volume(radius_cubed, factor_4_3, pi_value)

    # Step 5: Return the result.
    # No further processing (like rounding) is performed unless specified,
    # as the problem requires exact matches against high-precision assertions.
    return sphere_volume