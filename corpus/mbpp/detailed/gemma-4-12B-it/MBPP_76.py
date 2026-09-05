from typing import List

def count_Squares(width: int, height: int) -> int:
    """
    Calculates the total number of squares of all possible sizes 
    that can be found within a rectangle of dimensions width x height.

    A square of size k x k exists if k <= min(width, height).
    The number of such squares for a specific k is (width - k + 1) * (height - k + 1).

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Returns:
        int: The total count of squares.

    Raises:
        ValueError: If width or height are not non-negative integers.
    """
    # --- Input Validation ---
    # Ensure inputs are integers
    if not isinstance(width, int) or not isinstance(height, int):
        raise ValueError("Dimensions must be integers.")

    # Ensure dimensions are non-negative
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative.")

    # --- Handle Degenerate Cases ---
    # If either dimension is 0, no squares can exist.
    if width == 0 or height == 0:
        return 0

    # --- Core Logic ---
    # The maximum possible side length of a square is the smaller of the two dimensions.
    max_side_length = min(width, height)

    total_squares_count = 0

    # We iterate through every possible square side length 'k' from 1 up to max_side_length.
    # For a side length k, a square can start at any position (x, y) such that
    # 0 <= x <= width - k  and  0 <= y <= height - k.
    # The number of such starting positions is (width - k + 1) * (height - k + 1).
    for k in range(1, max_side_length + 1):
        # Calculate how many positions are available horizontally
        horizontal_positions = width - k + 1

        # Calculate how many positions are available vertically
        vertical_positions = height - k + 1

        # The number of squares of size k x k is the product of these positions
        squares_of_size_k = horizontal_positions * vertical_positions

        # Accumulate the total
        total_squares_count += squares_of_size_k

    return total_squares_count

if __name__ == "__main__":
    # Verification based on provided assertions
    assert count_Squares(4, 3) == 20
    assert count_Squares(2, 2) == 5
    assert count_Squares(1, 1) == 1