import math

def lateralsurface_cube(side_length: float) -> float:
    """
    Calculates the lateral surface area of a cube.

    The lateral surface area of a cube is the area of the four vertical faces,
    excluding the top and bottom bases. 
    Formula: Lateral Surface Area = 4 * (side_length^2)

    Args:
        side_length (float/int): The length of one edge of the cube.

    Returns:
        float: The lateral surface area of the cube.

    Raises:
        ValueError: If the side_length is negative.
        TypeError: If the input is not a number (int or float).
    """
    # Step 1: Validate input type
    # We ensure the input is either an integer or a floating point number.
    if not isinstance(side_length, (int, float)):
        raise TypeError(
            f"Input must be a numeric value (int or float), "
            f"but received {type(side_length).__name__}."
        )

    # Step 2: Validate input value
    # A cube cannot have a negative side length.
    # A side length of 0 is geometrically degenerate but mathematically valid (area = 0).
    if side_length < 0:
        raise ValueError(
            f"Side length cannot be negative. Received: {side_length}"
        )

    # Step 3: Handle the zero case explicitly
    # If the side length is 0, the surface area is 0.
    if side_length == 0:
        return 0.0

    # Step 4: Calculate the area of a single face
    # Area of a square face = side_length * side_length
    face_area = float(side_length ** 2)

    # Step 5: Calculate the lateral surface area
    # A cube has 6 faces total. The lateral surface area consists of 4 faces.
    number_of_lateral_faces = 4
    lateral_surface_area = number_of_lateral_faces * face_area

    # Step 6: Return the final result
    return lateral_surface_area

# The following assertions verify the correctness of the implementation
if __name__ == "__main__":
    # Test Case 1: Side length 5
    # 4 * (5^2) = 4 * 25 = 100
    assert lateralsurface_cube(5) == 100

    # Test Case 2: Side length 9
    # 4 * (9^2) = 4 * 81 = 324
    assert lateralsurface_cube(9) == 324

    # Test Case 3: Side length 10
    # 4 * (10^2) = 4 * 100 = 400
    assert lateralsurface_cube(10) == 400