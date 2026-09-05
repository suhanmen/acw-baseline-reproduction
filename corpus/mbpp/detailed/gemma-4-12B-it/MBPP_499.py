import math
from typing import Union

def diameter_circle(radius: Union[int, float]) -> Union[int, float]:
    """
    Calculates the diameter of a circle given its radius.

    The diameter is defined as twice the radius (d = 2r).

    Args:
        radius (Union[int, float]): The radius of the circle. 
                                     Must be a non-negative number.

    Returns:
        Union[int, float]: The diameter of the circle.

    Raises:
        TypeError: If the input is not an integer or a float.
        ValueError: If the input radius is negative.
    """

    # --- Input Validation ---

    # Check if the input is a valid numeric type
    if not isinstance(radius, (int, float)):
        raise TypeError(
            f"Input must be an integer or a float, but received {type(radius).__name__}."
        )

    # Check for negative radius as a circle cannot have a negative radius
    if radius < 0:
        raise ValueError(
            f"Radius cannot be negative. Received: {radius}"
        )

    # --- Logic ---

    # Handle the case of a zero radius (a point circle)
    if radius == 0:
        diameter = 0
        return diameter

    # The diameter is calculated by multiplying the radius by 2
    multiplier: int = 2
    diameter: Union[int, float] = radius * multiplier

    return diameter

# Assertion tests to verify correctness
if __name__ == "__main__":
    # The following assertions verify the requirements provided in the problem statement.
    assert diameter_circle(10) == 20
    assert diameter_circle(40) == 80
    assert diameter_circle(15) == 30