import math

def count_Squares(width: int, height: int) -> int:
    """
    Calculates the total number of squares of any size that can fit 
    within a rectangle of given width and height.

    A square of side length 'k' can be placed in a rectangle of 
    dimensions W x H if and only if k <= W and k <= H.
    The number of such squares of side length 'k' is (W - k + 1) * (H - k + 1).

    The total count is the sum of these values for all possible k starting from 1 
    up to the minimum dimension of the rectangle.
    """

    # --- Input Validation ---

    # Check if inputs are integers
    if not isinstance(width, int) or not isinstance(height, int):
        raise TypeError("Both width and height must be integers.")

    # Check if dimensions are non-negative
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative integers.")

    # --- Edge Case Handling ---

    # If either dimension is zero, no squares can exist.
    if width == 0 or height == 0:
        return 0

    # If both dimensions are zero (already handled by the above, but for clarity)
    if width == 0 and height == 0:
        return 0

    # --- Logic Implementation ---

    # The maximum possible side length of a square is the smaller of the two dimensions.
    max_side_length = min(width, height)

    total_squares_count = 0

    # Iterate through every possible side length 'k' from 1 to max_side_length.
    # Example: In a 4x3 rectangle, squares can have sides 1, 2, and 3.
    for k in range(1, max_side_length + 1):

        # Number of squares of side 'k' that can be placed horizontally:
        # If width is 4 and k is 1, we can place squares starting at indices 0, 1, 2, 3.
        # Formula: (Width - k + 1)
        horizontal_positions = width - k + 1

        # Number of squares of side 'k' that can be placed vertically:
        # If height is 3 and k is 1, we can place squares starting at indices 0, 1, 2.
        # Formula: (Height - k + 1)
        vertical_positions = height - k + 1

        # The number of squares of size k x k is the product of horizontal and vertical positions.
        squares_of_size_k = horizontal_positions * vertical_positions

        # Accumulate the total count.
        total_squares_count += squares_of_size_k

    return total_squares_count

# Verification against provided assertions:
# count_Squares(4, 3):
# k=1: (4-1+1)*(3-1+1) = 4*3 = 12
# k=2: (4-2+1)*(3-2+1) = 3*2 = 6
# k=3: (4-3+1)*(3-3+1) = 2*1 = 2
# Total: 12 + 6 + 2 = 20. Correct.

# count_Squares(1, 2):
# k=1: (1-1+1)*(2-1+1) = 1*2 = 2
# Total: 2. Correct.

# count_Squares(2, 2):
# k=1: (2-1+1)*(2-1+1) = 2*2 = 4
# k=2: (2-2+1)*(2-2+1) = 1*1 = 1
# Total: 4 + 1 = 5. Correct.