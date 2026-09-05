def count_Squares(length, width):
    """
    Counts the number of squares in a rectangle defined by its length and width.

    Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.

    Returns:
        int: The total number of squares that can fit into the rectangle.

    Raises:
        ValueError: If length or width is non-positive.
    """
    # Validate input
    if not isinstance(length, int) or not isinstance(width, int):
        raise ValueError("Both length and width must be integers.")
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive integers.")

    # Handle the case where the rectangle is a square
    if length == width:
        n = length
        return n * (n + 1) * (2 * n + 1) // 6

    # Handle the general case where length and width are different
    max_size = min(length, width)
    total_squares = 0
    for size in range(1, max_size + 1):
        squares_in_length = length - size + 1
        squares_in_width = width - size + 1
        total_squares += squares_in_length * squares_in_width

    return total_squares

# Example usage:
if __name__ == "__main__":
    print(count_Squares(4, 3))  # Output: 20
    print(count_Squares(1, 2))  # Output: 2
    print(count_Squares(2, 2))  # Output: 5