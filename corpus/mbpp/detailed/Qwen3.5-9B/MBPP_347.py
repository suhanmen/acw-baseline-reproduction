from typing import Tuple, Union

Number = Union[int, float]

def _validate_dimensions(width: Number, height: Number) -> Tuple[Number, Number]:
    """
    Validate that the provided width and height are positive numbers.

    Returns a tuple of (width, height) with the dimensions swapped if necessary
    to ensure width >= height, which simplifies the counting logic.

    Raises:
        TypeError: If inputs are not numbers.
        ValueError: If inputs are not positive.
    """
    # Check for valid types
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Dimensions must be integers or floats.")

    # Check for positive values
    if width <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    if height <= 0:
        raise ValueError("Dimensions must be positive numbers.")

    # Ensure width is the larger dimension for consistent logic
    if width < height:
        return height, width
    return width, height

def _count_squares_for_n(width: Number, height: Number) -> Number:
    """
    Helper function to calculate the number of squares with a specific side length 'n'
    that can fit inside a rectangle of given width and height.

    If a square has side length 'n', it requires at least 'n' units of width
    and 'n' units of height. The number of such squares is determined by:
    (number of positions horizontally) * (number of positions vertically)
    = (width - n + 1) * (height - n + 1)

    If n is larger than either dimension, no such squares can exist.

    Args:
        width: The width of the rectangle (guaranteed >= height).
        height: The height of the rectangle (guaranteed <= width).
        n: The side length of the square.

    Returns:
        The count of squares of size n x n that fit in the rectangle.
    """
    # Ensure n is valid for the calculation (must be positive)
    if n <= 0:
        return 0

    # If the square side is larger than the height (the smaller dimension),
    # no square of this size can fit.
    if n > height:
        return 0

    # Calculate horizontal positions: (width - n + 1)
    horizontal_positions = width - n + 1

    # Calculate vertical positions: (height - n + 1)
    vertical_positions = height - n + 1

    # The total count is the product of horizontal and vertical positions
    total_count = horizontal_positions * vertical_positions

    return total_count

def count_Squares(width: Number, height: Number) -> int:
    """
    Counts the total number of squares (of all possible sizes) that can fit
    inside a rectangle of the given width and height.

    The algorithm iterates through every possible square side length 'n' from 1
    up to the smaller dimension of the rectangle. For each 'n', it calculates
    how many squares of that specific size fit, and sums these counts together.

    Args:
        width: The width of the rectangle. Must be a positive number.
        height: The height of the rectangle. Must be a positive number.

    Returns:
        The total integer count of all squares that fit in the rectangle.

    Raises:
        TypeError: If width or height are not numbers.
        ValueError: If width or height are not positive.
    """
    # Step 1: Validate and normalize inputs
    normalized_width, normalized_height = _validate_dimensions(width, height)

    # Identify the smaller dimension as the loop limit
    # Since we ensured normalized_width >= normalized_height:
    limit = normalized_height

    # Initialize total accumulator
    total_squares = 0

    # Step 2: Iterate through all possible square side lengths from 1 to the limit
    for n in range(1, int(limit) + 1):
        # Calculate count for current square size 'n'
        count_for_n = _count_squares_for_n(normalized_width, normalized_height, n)

        # Add to the running total
        total_squares += count_for_n

    # Return the final accumulated result
    return int(total_squares)