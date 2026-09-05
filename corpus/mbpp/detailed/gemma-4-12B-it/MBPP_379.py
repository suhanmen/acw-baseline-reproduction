from typing import Union

def surfacearea_cuboid(length: Union[int, float], width: Union[int, float], height: Union[int, float]) -> Union[int, float]:
    """
    Calculates the surface area of a cuboid given its length, width, and height.

    The surface area of a cuboid is calculated using the formula:
    Surface Area = 2 * (length * width + width * height + height * length)

    Args:
        length (Union[int, float]): The length of the cuboid.
        width (Union[int, float]): The width of the cuboid.
        height (Union[int, float]): The height of the cuboid.

    Returns:
        Union[int, float]: The total surface area.

    Raises:
        ValueError: If any dimension is non-positive.
        TypeError: If any input is not an integer or a float.
    """

    # Define a helper function to validate inputs
    def validate_dimension(dim: Union[int, float], name: str) -> None:
        # Check for correct types
        if not isinstance(dim, (int, float)):
            raise TypeError(f"Dimension '{name}' must be a number, received {type(dim).__name__}.")

        # Check for physical feasibility (dimensions must be positive)
        # Note: A cuboid with a dimension of 0 has 0 surface area in some contexts,
        # but mathematically, a cuboid is a 3D shape, so dimensions should be > 0.
        if dim <= 0:
            raise ValueError(f"Dimension '{name}' must be greater than zero. Received: {dim}")

    # Validate all inputs before performing calculations
    validate_dimension(length, "length")
    validate_dimension(width, "width")
    validate_dimension(height, "height")

    # Calculate individual face areas
    # A cuboid has 3 pairs of identical faces:
    # 1. Bottom and Top
    area_bottom_top = length * width

    # 2. Front and Back
    area_front_back = length * height

    # 3. Left and Right sides
    area_left_right = width * height

    # Sum the areas of one of each face type
    sum_of_unique_faces = area_bottom_top + area_front_back + area_left_right

    # The total surface area is twice the sum of the three unique faces
    total_surface_area = 2 * sum_of_unique_faces

    return total_surface_area

if __name__ == "__main__":
    # Standard assertions provided in the problem description
    assert surfacearea_cuboid(1, 2, 3) == 22
    assert surfacearea_cuboid(5, 7, 9) == 286
    assert surfacearea_cuboid(10, 15, 21) == 1350