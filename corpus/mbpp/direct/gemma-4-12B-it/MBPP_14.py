def find_Volume(base_length, base_height, height):
    """
    Calculates the volume of a triangular prism.
    Formula: Volume = (base_length * base_height / 2) * height

    Args:
        base_length (float): The length of the base of the triangular face.
        base_height (float): The height of the triangular face.
        height (float): The length (height) of the prism.

    Returns:
        float: The volume of the triangular prism.
    """
    volume = (0.5 * base_length * base_height) * height
    return volume

if __name__ == "__main__":
    assert find_Volume(10, 8, 6) == 240
    assert find_Volume(3, 2, 2) == 6
    assert find_Volume(1, 2, 1) == 1