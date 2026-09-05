import math
from typing import Union

def area_pentagon(side_length: Union[int, float]) -> float:
    """
    Calculates the area of a regular pentagon given the length of one side.

    The formula for the area of a regular pentagon is:
    Area = (1/4) * sqrt(5 * (5 + 2 * sqrt(5))) * side_length^2

    Alternatively expressed as:
    Area = (side_length^2 * 5) / (4 * tan(pi / 5))

    Args:
        side_length: The length of one side of the regular pentagon.
                     Must be a non-negative number.

    Returns:
        float: The calculated area of the pentagon.

    Raises:
        ValueError: If the side_length is negative.
        TypeError: If the side_length is not an integer or a float.
    """
    # Step 1: Input Validation
    # Ensure the input is of a numeric type (int or float)
    if not isinstance(side_length, (int, float)):
        raise TypeError(f"Input must be a number, received {type(side_length).__name__}")

    # Ensure the input is non-negative
    # A pentagon cannot have a negative side length.
    if side_length < 0:
        raise ValueError(f"Side length cannot be negative. Received: {side_length}")

    # Step 2: Handle degenerate cases
    # A pentagon with side length 0 has an area of 0.
    if side_length == 0:
        return 0.0

    # Step 3: Perform calculations
    # We use the formula: Area = (5 * s^2) / (4 * tan(pi / 5))
    # pi / 5 radians is the central angle / 2 or related to the interior angles.

    # Constants
    num_sides = 5
    pi_value = math.pi

    # Intermediate values for the formula
    # Area = (n * s^2) / (4 * tan(pi / n))
    side_squared = float(side_length ** 2)

    # Calculate the denominator: 4 * tan(pi / 5)
    angle_in_radians = pi_value / num_sides
    tangent_value = math.tan(angle_in_radians)
    denominator = 4.0 * tangent_value

    # Calculate numerator: 5 * s^2
    numerator = float(num_sides) * side_squared

    # Final area calculation
    area = numerator / denominator

    return area

if __name__ == "__main__":
    # The following assertions verify the requirements provided in the prompt.
    # Using math.isclose for float comparison to account for precision,
    # although the problem specifies exact equality for these specific values.

    res1 = area_pentagon(5)
    assert math.isclose(res1, 43.01193501472417, rel_tol=1e-12)

    res2 = area_pentagon(10)
    assert math.isclose(res2, 172.0477400588967, rel_tol=1e-12)

    res3 = area_pentagon(15)
    assert math.isclose(res3, 387.10741513251753, rel_tol=1e-12)