def substract_elements(a, b):
    """
    Subtracts the contents of one tuple from another, element-wise.

    Parameters:
    a (tuple): The first tuple of integers.
    b (tuple): The second tuple of integers.

    Returns:
    tuple: A new tuple where each element is the result of subtracting corresponding elements.

    Raises:
    ValueError: If inputs are not valid tuples or if they are of different lengths.

    Examples:
    substract_elements((10, 4, 5), (2, 5, 18)) returns (8, -1, -13)
    substract_elements((11, 2, 3), (24, 45, 16)) returns (-13, -43, -13)
    substract_elements((7, 18, 9), (10, 11, 12)) returns (-3, 7, -3)
    """
    # Validate inputs
    if not isinstance(a, tuple) or not isinstance(b, tuple):
        raise ValueError("Both inputs must be tuples.")
    if len(a) != len(b):
        raise ValueError("Tuples must be of the same length.")

    # Helper function to perform element-wise subtraction
    def subtract_elements(x, y):
        return tuple(x_i - y_i for x_i, y_i in zip(x, y))

    return subtract_elements(a, b)