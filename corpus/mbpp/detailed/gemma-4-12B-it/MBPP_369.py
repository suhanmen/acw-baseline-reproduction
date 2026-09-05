from typing import Union

def lateralsurface_cuboid(length: Union[int, float], 
                           width: Union[int, float], 
                           height: Union[int, float]) -> Union[int, float]:
    """
    Calculates the lateral surface area of a cuboid.

    The lateral surface area is the area of the four vertical faces of the cuboid,
    excluding the top and bottom faces.
    Formula: Lateral Surface Area = 2 * height * (length + width)

    Args:
        length: The length of the base of the cuboid.
        width: The width of the base of the cuboid.
        height: The height of the cuboid.

    Returns:
        The lateral surface area as an int or float.

    Raises:
        ValueError: If any of the dimensions are non-positive.
        TypeError: If any of the dimensions are not numeric.
    """

    # Validate that inputs are of the correct type (int or float)
    inputs = {"length": length, "width": width, "height": height}
    for name, value in inputs.items():
        if not isinstance(value, (int, float)):
            raise TypeError(f"The input '{name}' must be a numeric type (int or float), got {type(value).__name__}.")

    # Validate that dimensions are positive numbers
    # A cuboid with zero or negative dimensions is physically impossible in this context.
    if length <= 0:
        raise ValueError(f"Length must be positive. Received: {length}")
    if width <= 0:
        raise ValueError(f"Width must be positive. Received: {width}")
    if height <= 0:
        raise ValueError(f"Height must be positive. Received: {height}")

    # Step 1: Calculate the perimeter of the base
    # Perimeter = 2 * (length + width)
    base_sum = length + width
    base_perimeter = 2 * base_sum

    # Step 2: Calculate the lateral surface area
    # Lateral Surface Area = Perimeter of base * height
    lateral_area = base_perimeter * height

    # Ensure the result is returned in a clean format
    # If the inputs were integers and the result is a whole number, return an int.
    if isinstance(length, int) and isinstance(width, int) and isinstance(height, int):
        if lateral_area == int(lateral_area):
            return int(lateral_area)

    return lateral_area

if __name__ == "__main__":
    # Assertions provided in the problem description
    assert lateralsurface_cuboid(8, 5, 6) == 156
    assert lateralsurface_cuboid(7, 9, 10) == 320
    assert lateralsurface_cuboid(10, 20, 30) == 1800