def find_Volume(base, side_height, prism_height):
    # Validate the inputs
    if not (isinstance(base, (int, float)) and isinstance(side_height, (int, float)) and isinstance(prism_height, (int, float))):
        raise ValueError("All inputs must be numbers")

    if base <= 0 or side_height <= 0 or prism_height <= 0:
        raise ValueError("Base, side height, and prism height must be positive numbers")

    # Calculate the base area of the triangle
    base_area = 0.5 * base * side_height

    # Calculate the volume of the prism
    volume = base_area * prism_height

    return volume