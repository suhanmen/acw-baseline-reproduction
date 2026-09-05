from typing import Union

def surfacearea_cube(side_length: Union[int, float]) -> float:
    """
    Calculates the surface area of a cube given the length of one side.

    The surface area of a cube is calculated as:
    Area = 6 * (side_length^2)

    Args:
        side_length (Union[int, float]): The length of one side of the cube.

    Returns:
        float: The total surface area of the cube.

    Raises:
        ValueError: If the side_length is negative.
        TypeError: If the side_length is not a numeric type.
    """

    # --- Input Validation ---

    # Check if the input type is numeric (int or float)
    # Using isinstance to allow for both types while excluding strings or None
    if not isinstance(side_length, (int, float)):
        raise TypeError(
            f"Invalid input type: {type(side_length).__name__}. "
            "Side length must be an integer or a float."
        )

    # Check for negative values
    # A geometric shape cannot have a negative side length.
    if side_length < 0:
        raise ValueError(
            f"Invalid input value: {side_length}. "
            "Side length cannot be negative."
        )

    # --- Calculation Logic ---

    # Handle the degenerate case of a side length of zero
    # A cube with side 0 has surface area 0.
    if side_length == 0:
        return 0.0

    # Step 1: Calculate the area of a single face.
    # The area of a square face is side * side.
    face_area = float(side_length * side_length)

    # Step 2: Calculate the total surface area.
    # A cube has 6 identical faces.
    total_surface_area = 6.0 * face_area

    return total_surface_area

# The following assertions verify the correctness of the function.
if __name__ == "__main__":
    assert surfacearea_cube(5) == 150
    assert surfacearea_cube(3) == 54
    assert surfacearea_cube(10) == 600