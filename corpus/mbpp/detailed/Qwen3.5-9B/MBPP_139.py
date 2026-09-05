import math
from typing import Union

def _validate_radius(radius: Union[int, float]) -> None:
    """
    Validates that the provided radius is a valid non-negative number.

    Arguments:
        radius: The input value intended to be the radius of the circle.

    Raises:
        TypeError: If the input is not an integer or a float.
        ValueError: If the input is negative.
    """
    # Check for type validity explicitly
    if not isinstance(radius, (int, float)):
        raise TypeError(
            f"Expected radius to be an integer or float, but got {type(radius).__name__}."
        )

    # Check for negative values explicitly
    if radius < 0:
        raise ValueError(
            f"Radius cannot be negative. Received value: {radius}"
        )


def _calculate_circumference(radius: Union[int, float]) -> float:
    """
    Calculates the circumference of a circle given a valid radius.

    Formula: C = 2 * π * r

    Arguments:
        radius: The valid, non-negative radius of the circle.

    Returns:
        The calculated circumference as a float.
    """
    pi_value = math.pi
    two = 2.0

    # Perform the calculation using explicit intermediate steps
    diameter = two * radius
    circumference = pi_value * diameter

    return circumference


def circle_circumference(radius: Union[int, float]) -> float:
    """
    Calculates and returns the circumference of a circle based on the given radius.

    This function validates the input to ensure it represents a geometrically valid
    radius (a real number >= 0). It then computes the circumference using the
    standard mathematical formula C = 2 * π * r.

    Special cases handled:
        - Empty input is not possible due to type system, but non-numeric types are rejected.
        - Single element (radius) is processed normally.
        - Zero radius results in a circumference of 0.0.
        - All-equal elements logic is not applicable here as it is a single value function,
          but repeated calls with the same value will yield identical results.
        - Negative numbers and boundary values (like very large or very small floats)
          are checked for validity and handled accordingly (rejected if negative).

    Arguments:
        radius: The radius of the circle. Must be a non-negative number (int or float).

    Returns:
        The circumference of the circle.

    Raises:
        TypeError: If the radius is not an integer or a float.
        ValueError: If the radius is negative.
    """
    # Step 1: Validate the input explicitly
    _validate_radius(radius)

    # Step 2: Calculate the circumference using the helper function
    result = _calculate_circumference(radius)

    # Step 3: Return the result
    return result