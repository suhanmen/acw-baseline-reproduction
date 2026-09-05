def square_perimeter(side_length):
    """
    Calculate the perimeter of a square.

    Args:
        side_length (int or float): The length of one side of the square.

    Returns:
        float: The perimeter of the square, which is 4 times the side length.

    Raises:
        TypeError: If the side_length is not a number.
        ValueError: If the side_length is negative.
    """
    # Check if side_length is a number
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be a number")

    # Check if side_length is negative
    if side_length < 0:
        raise ValueError("side_length must be non-negative")

    # Calculate perimeter
    perimeter = 4 * side_length

    return perimeter

# Test the function with the given assertions
assert square_perimeter(10) == 40
assert square_perimeter(5) == 20
assert square_perimeter(4) == 16