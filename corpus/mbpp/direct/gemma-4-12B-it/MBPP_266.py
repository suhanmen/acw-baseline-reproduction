def lateralsurface_cube(side_length):
    """
    Calculates the lateral surface area of a cube.
    The lateral surface area of a cube is the area of the four vertical faces.
    Formula: 4 * (side_length^2)
    """
    return 4 * (side_length ** 2)

if __name__ == "__main__":
    assert lateralsurface_cube(5) == 100
    assert lateralsurface_cube(9) == 324
    assert lateralsurface_cube(10) == 400