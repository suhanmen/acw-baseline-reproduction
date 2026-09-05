def array_3d(x, y, z):
    """
    Generates a 3D array (list of lists of lists) with dimensions x, y, z
    where each element is '*'.

    Based on the provided assertions:
    assert array_3d(6,4,3) -> result shape is (3, 4, 6)
    assert array_3d(5,3,4) -> result shape is (4, 3, 5)
    assert array_3d(1,2,3) -> result shape is (3, 2, 1)

    The pattern from the assertions is:
    The first argument (x) becomes the inner-most dimension.
    The second argument (y) becomes the middle dimension.
    The third argument (z) becomes the outer-most dimension.
    """
    return [[['*' for _ in range(x)] for _ in range(y)] for _ in range(z)]