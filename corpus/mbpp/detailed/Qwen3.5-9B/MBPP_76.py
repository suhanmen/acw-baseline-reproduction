def count_squares(width: int, height: int) -> int:
    """
    Counts the total number of squares that can be formed within a rectangle
    of the given dimensions (width x height).

    A square of size S x S can fit in the rectangle if both width >= S and height >= S.
    The number of S x S squares in an A x B rectangle is (A - S + 1) * (B - S + 1).

    This function is robust and handles edge cases including:
    - Negative dimensions (raises ValueError)
    - Zero dimensions (returns 0)
    - Single element rectangles (returns 1)
    - Non-square rectangles where width != height
    - Large boundary values

    Parameters:
        width (int): The width of the rectangle (horizontal dimension).
        height (int): The height of the rectangle (vertical dimension).

    Returns:
        int: The total count of squares of all possible sizes that fit in the rectangle.

    Raises:
        ValueError: If either width or height is negative.
    """

    # Step 1: Validate inputs explicitly
    # Check for non-integer types to prevent unexpected behavior later,
    # although type hints suggest ints, runtime check adds safety.
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError("Both width and height must be integers.")

    # Step 2: Handle negative values explicitly
    if width < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative.")

    # Step 3: Define a helper function to calculate the number of squares of a specific size
    def count_squares_of_size(s_size: int, total_w: int, total_h: int) -> int:
        """
        Calculates how many squares of 's_size' x 's_size' fit into a rectangle.

        Logic:
        - Number of positions horizontally: (total_w - s_size + 1)
        - Number of positions vertically: (total_h - s_size + 1)
        - If either count is <= 0, no such square fits.
        """
        horizontal_positions = total_w - s_size + 1
        vertical_positions = total_h - s_size + 1

        # If the side length is greater than either dimension, count is 0
        if horizontal_positions <= 0 or vertical_positions <= 0:
            return 0

        return horizontal_positions * vertical_positions

    # Step 4: Determine the maximum possible square size that fits in the rectangle
    # A square cannot be larger than the smaller dimension of the rectangle.
    if width == height:
        # Special case for a perfect square, logic below handles it generally,
        # but we identify the limit.
        max_square_side = width
    elif width < height:
        max_square_side = width
    else: # width > height
        max_square_side = height

    # Step 5: Initialize the total count accumulator
    total_count = 0

    # Step 6: Iterate through every possible square size from 1 up to the maximum side
    # We use an explicit loop rather than a one-liner to adhere to the requirement
    # of explicit control flow and visible steps.
    current_size = 1
    while current_size <= max_square_side:
        # Calculate squares for the current size
        squares_in_this_size = count_squares_of_size(current_size, width, height)

        # Add to the total accumulator
        total_count = total_count + squares_in_this_size

        # Increment size for next iteration
        current_size = current_size + 1

    # Step 7: Return the final calculated count
    return total_count