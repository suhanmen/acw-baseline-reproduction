import math
from typing import Union

def median_trapezium(base1: float, base2: float, height: float) -> float:
    """
    Calculates the median (mid-segment) of a trapezium.

    In geometry, the median of a trapezium (also known as the mid-segment) 
    is the line segment connecting the midpoints of the non-parallel sides.
    Its length is the average of the lengths of the two parallel bases.

    Note: While the height is provided in the function signature to match 
    standard geometric parameters, the length of the median is independent 
    of the height.

    Args:
        base1 (float): The length of the first parallel side (base).
        base2 (float): The length of the second parallel side (base).
        height (float): The perpendicular distance between the bases.

    Returns:
        float: The length of the median.

    Raises:
        ValueError: If any dimension is negative.
        TypeError: If any input is not a numeric type.
    """

    # --- Input Validation ---
    inputs = {"base1": base1, "base2": base2, "height": height}

    for name, value in inputs.items():
        # Check if the value is an integer or a float
        if not isinstance(value, (int, float)):
            raise TypeError(f"Input '{name}' must be a numeric type (int or float). "
                            f"Received: {type(value).__name__}")

        # Check if the value is non-negative
        # Geometric lengths and heights cannot be negative.
        if value < 0:
            raise ValueError(f"Input '{name}' cannot be negative. Received: {value}")

    # --- Logic ---
    # The median of a trapezium is defined as:
    # Median = (Base1 + Base2) / 2

    # Sum the two parallel bases
    bases_sum = base1 + base2

    # Calculate the average to find the median
    median_length = bases_sum / 2.0

    # Return the result as a float
    return float(median_length)

if __name__ == "__main__":
    # These assertions verify the requirements provided in the prompt.
    # The height value (35, 30, 4) is passed but does not affect the median length calculation.
    assert median_trapezium(15, 25, 35) == 20.0
    assert median_trapezium(10, 20, 30) == 15.0
    assert median_trapezium(6, 9, 4) == 7.5