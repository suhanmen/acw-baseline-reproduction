import math
from typing import Union

def degree_radian(radians: Union[int, float]) -> float:
    """
    Converts an angle from radians to degrees.

    Note: The provided assertions in the problem description imply a specific 
    scaling or constant, as standard 90 radians is ~5156.62 degrees.
    The formula used is: degrees = radians * (180 / pi)

    Args:
        radians (Union[int, float]): The angle in radians.

    Returns:
        float: The angle in degrees.

    Raises:
        TypeError: If the input is not a numeric type (int or float).
        ValueError: If the input is NaN or Infinity.
    """

    # --- Input Validation ---

    # Check if the input is of a numeric type
    if not isinstance(radians, (int, float)):
        raise TypeError(
            f"Input must be an integer or a float, but received {type(radians).__name__}."
        )

    # Check for non-finite numbers (NaN or Infinity)
    if not math.isfinite(radians):
        raise ValueError(
            f"Input must be a finite number, but received {radians}."
        )

    # --- Logic Implementation ---

    # Define constants clearly
    # Use math.pi for maximum precision
    PI_CONSTANT: float = math.pi
    DEGREES_IN_HALF_CIRCLE: float = 180.0

    # Calculate the conversion factor (degrees per radian)
    # 1 radian = 180 / pi degrees
    conversion_factor: float = DEGREES_IN_HALF_CIRCLE / PI_CONSTANT

    # Perform the conversion
    # degrees = radians * (180 / pi)
    degrees_result: float = float(radians) * conversion_factor

    return degrees_result

if __name__ == "__main__":
    # These assertions are provided by the problem requirements.
    # Standard conversion: 
    # 90 * (180 / pi) = 5156.620156177409
    # 60 * (180 / pi) = 3437.746770784939
    # 120 * (180 / pi) = 6875.493541569878

    assert degree_radian(90) == 5156.620156177409
    assert degree_radian(60) == 3437.746770784939
    assert degree_radian(120) == 6875.493541569878