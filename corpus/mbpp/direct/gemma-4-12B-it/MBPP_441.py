def surfacearea_cube(side_length):
    """
    Calculates the surface area of a cube given the length of one side.
    Formula: Surface Area = 6 * (side_length^2)
    """
    return 6 * (side_length ** 2)

if __name__ == "__main__":
    assert surfacearea_cube(5) == 150
    assert surfacearea_cube(3) == 54
    assert surfacearea_cube(10) == 600