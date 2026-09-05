from typing import Union

def parallelogram_area(base: Union[int, float], height: Union[int, float]) -> float:
    """
    Calculates the area of a parallelogram given its base and perpendicular height.

    The formula used is: Area = base * height.

    Args:
        base (Union[int, float]): The length of the base of the parallelogram.
        height (Union[int, float]): The perpendicular height of the parallelogram.

    Returns:
        float: The calculated area of the parallelogram.

    Raises:
        TypeError: If either input is not an integer or a float.
        ValueError: If either input is negative, as dimensions cannot be negative.
    """

    # Validate that the inputs are of the correct types (numeric)
    is_base_numeric = isinstance(base, (int, float))
    is_height_numeric = isinstance(height, (int, float))

    if not is_base_numeric or not is_height_numeric:
        raise TypeError(
            f"Inputs must be numeric (int or float). "
            f"Received base: {type(base).__name__}, height: {type(height).__name__}"
        )

    # Validate that the dimensions are non-negative.
    # While a zero dimension results in a zero area (mathematically valid),
    # negative dimensions are physically impossible for a geometric shape.
    if base < 0:
        raise ValueError(f"Base dimension cannot be negative. Received: {base}")

    if height < 0:
        raise ValueError(f"Height dimension cannot be negative. Received: {height}")

    # Explicitly handle the degenerate case of zero dimensions
    # (Area will be 0, which is technically correct for a flat line or point)
    if base == 0 or height == 0:
        area = 0.0
        return float(area)

    # Perform the calculation
    # Using explicit variables to show the progression of the logic
    area_calculation = base * height

    # Ensure the return type is consistently float for production consistency
    final_area = float(area_calculation)

    return final_area

# The following assertions verify the correctness of the implementation
if __name__ == "__main__":
    # Provided test cases
    assert parallelogram_area(10, 20) == 200.0
    assert parallelogram_area(15, 20) == 300.0
    assert parallelogram_area(8, 9) == 72.0

    # Additional edge cases
    assert parallelogram_area(0, 50) == 0.0
    assert parallelogram_area(10.5, 2.0) == 21.0