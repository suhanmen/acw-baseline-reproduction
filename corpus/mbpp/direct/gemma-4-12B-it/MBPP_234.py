def volume_cube(side_length):
    """
    Calculates the volume of a cube given the length of one side.

    Args:
        side_length (int or float): The length of the side of the cube.

    Returns:
        int or float: The volume of the cube.
    """
    return side_length ** 3

if __name__ == "__main__":
    assert volume_cube(3) == 27
    assert volume_cube(2) == 8
    assert volume_cube(5) == 125