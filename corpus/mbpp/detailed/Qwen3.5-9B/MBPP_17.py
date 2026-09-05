def square_perimeter(side_length):
    """
    Calculate the perimeter of a square given the length of one of its sides.

    The perimeter of a square is defined as the total distance around the square.
    Since a square has four equal sides, the perimeter is calculated as 4 times
    the length of one side.

    Parameters:
    side_length (float or int): The length of one side of the square.
                                Must be a non-negative number.

    Returns:
    float: The perimeter of the square.

    Raises:
    TypeError: If side_length is not a number (int or float).
    ValueError: If side_length is negative.
    """

    # Step 1: Validate the input type.
    # We explicitly check if the input is an integer or a float to ensure
    # we are dealing with numerical data as expected for a geometric measurement.
    if not isinstance(side_length, (int, float)):
        raise TypeError(
            f"Expected side_length to be a number (int or float), "
            f"but got type: {type(side_length).__name__}"
        )

    # Step 2: Validate the input value.
    # A physical side length cannot be negative. Zero is mathematically valid 
    # for a degenerate case (a point), but often implies no perimeter in physical contexts.
    # We enforce non-negative values as per standard geometric definitions for positive areas/perimeters.
    if side_length < 0:
        raise ValueError(
            f"Side length must be non-negative, but got: {side_length}"
        )

    # Step 3: Declare an intermediate variable for the side length.
    # This makes the logic explicit and improves readability by separating 
    # the input parameter from the value used in calculation.
    current_side = side_length

    # Step 4: Calculate the perimeter using the explicit formula.
    # Perimeter = 4 * side_length
    # We use 4 explicitly rather than a constant variable to keep the logic 
    # transparent and self-documenting within the function body.
    perimeter_value = 4 * current_side

    # Step 5: Return the calculated result.
    # The function returns a float to handle cases where side_length is a float,
    # ensuring consistent numeric output types.
    return perimeter_value