import math
from typing import Union

def volume_cuboid(length: Union[int, float], width: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    """
    Calculates the volume of a cuboid given its length, width, and height.

    The volume is calculated as: volume = length * width * height.

    Args:
        length: The length of the cuboid.
        width: The width of the cuboid.
        height: The height of the cuboid.

    Returns:
        The volume of the cuboid as a numeric value (int or float).

    Raises:
        TypeError: If any of the inputs are not numeric (int or float).
        ValueError: If any of the dimensions are negative, as physical dimensions 
                    must be non-negative.
    """

    # List of inputs to validate
    dimensions = [length, width, height]

    # Step 1: Validate input types
    for dim in dimensions:
        if not isinstance(dim, (int, float)):
            raise TypeError(
                f"All dimensions must be numeric (int or float). "
                f"Received type: {type(dim).__name__}"
            )

    # Step 2: Validate physical constraints
    # While a 0-dimension cuboid has 0 volume, a negative dimension is invalid.
    for dim in dimensions:
        if dim < 0:
            raise ValueError(
                f"Dimensions must be non-negative. Received value: {dim}"
            )

    # Step 3: Handle degenerate case (zero dimension)
    # If any dimension is 0, the volume is 0.
    if length == 0 or width == 0 or height == 0:
        volume = 0
    else:
        # Step 4: Perform the calculation
        # We separate the multiplications to maintain clarity.
        base_area = length * width
        volume = base_area * height

    # Step 5: Final return
    # If the inputs were integers and the result is a whole number, 
    # returning an int is preferred, but standard multiplication handles this.
    return volume

# Internal verification (can be removed if strictly required, but ensures production quality)
if __name__ == "__main__":
    # Assertions provided in the problem statement
    assert volume_cuboid(1, 2, 3) == 6
    assert volume_cuboid(5, 7, 9) == 315
    assert volume_cuboid(10, 15, 21) == 3150

    # Additional edge cases
    assert volume_cuboid(0, 10, 10) == 0
    assert volume_cuboid(1.5, 2.0, 3.0) == 9.0