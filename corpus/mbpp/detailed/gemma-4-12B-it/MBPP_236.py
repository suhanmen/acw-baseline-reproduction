import math

def No_of_Triangle(side_length: int, sub_triangle_side: int) -> int:
    """
    Calculates the maximum number of equilateral triangles of a specific size 
    that can be formed within a larger equilateral triangle.

    Args:
        side_length (int): The side length of the large equilateral triangle.
        sub_triangle_side (int): The side length of the smaller equilateral triangles to count.

    Returns:
        int: The count of small equilateral triangles, or -1 if inputs are invalid
             or if the small triangle is larger than the large triangle.
    """

    # Step 1: Input Validation
    # Check if inputs are integers
    if not isinstance(side_length, int) or not isinstance(sub_triangle_side, int):
        return -1

    # Check for non-positive dimensions
    if side_length <= 0 or sub_triangle_side <= 0:
        return -1

    # Step 2: Feasibility Check
    # A triangle of size 'sub_triangle_side' cannot fit in 'side_length' 
    # if the sub_triangle is strictly larger.
    if sub_triangle_side > side_length:
        return -1

    # Step 3: Geometry Logic
    # Let N = side_length and n = sub_triangle_side.
    # The large triangle can be divided into (N/n)^2 smaller triangles of side length n.
    # However, the problem asks for the count of triangles of side length 'n' 
    # that can be formed. This includes both 'upright' and 'inverted' triangles.

    # Let K be the number of small units (triangles of size 1) along the side of the large triangle.
    # K = side_length // sub_triangle_side

    # In a triangle of side length K (measured in units of sub_triangle_side),
    # the number of "upright" triangles of side length 's' is:
    # (K - s + 1) * (K - s + 2) * (K - s + 3) // 6  -- This is incorrect for 2D tiling.

    # Correct approach for tiling:
    # If we divide the large triangle into a grid of unit triangles (side length 1),
    # and we want to count triangles of side length 'k'.
    # A triangle of side length 'k' can be placed such that its vertices are on 
    # the grid points.

    # Let L = side_length and s = sub_triangle_side.
    # The total number of triangles of side length s that can fit is:
    # Sum for i from 1 to (L - s + 1):
    # Each row i (where 1 is the top) can accommodate some number of triangles.
    # However, standard formula for triangles of side length 's' 
    # within a triangle of side length 'L' is:
    # Sum_{j=1}^{L-s+1} (j * (j+1) / 2) - (Wait, that's for all possible sizes).

    # Re-evaluating the specific requirements based on the test cases provided:
    # assert No_of_Triangle(4,2) == 7
    # assert No_of_Triangle(4,3) == 3
    # assert No_of_Triangle(1,3) == -1

    # Analysis of Case (4, 2):
    # L = 4, s = 2.
    # Upright triangles: 
    # Row 1 (top): 1 triangle (at top)
    # Row 2: 2 triangles
    # Row 3: 3 triangles
    # Total upright = 1 + 2 + 3 = 6.
    # Wait, the row height for a triangle of side 2 is 2 units.
    # Let's count manually for L=4, s=2:
    # The number of "upright" triangles of side s in a triangle of side L is:
    # Sum_{i=1}^{L-s+1} (i) = (L-s+1)(L-s+2)/2
    # For L=4, s=2: (4-2+1)(4-2+2)/2 = 3*4/2 = 6.
    # The number of "inverted" triangles of side s in a triangle of side L is:
    # Sum_{i=1}^{L-2s+1} (i) = (L-2s+1)(L-2s+2)/2
    # For L=4, s=2: (4-4+1)(4-4+2)/2 = 1*2/2 = 1.
    # Total = 6 + 1 = 7. Matches assertion!

    # Analysis of Case (4, 3):
    # L = 4, s = 3.
    # Upright: (4-3+1)(4-3+2)/2 = 2*3/2 = 3.
    # Inverted: (4-2*3+1) ... 4-6+1 = -1. (Since < 1, count is 0).
    # Total = 3 + 0 = 3. Matches assertion!

    # General Formula:
    # Count = Upright + Inverted
    # Upright = (L - s + 1) * (L - s + 2) / 2
    # Inverted = (L - 2s + 1) * (L - 2s + 2) / 2  (if L >= 2s, else 0)

    # Step 4: Calculation
    L = side_length
    s = sub_triangle_side

    # Calculate upright triangles
    num_upright_rows = L - s + 1
    if num_upright_rows > 0:
        upright_count = (num_upright_rows * (num_upright_rows + 1)) // 2
    else:
        upright_count = 0

    # Calculate inverted triangles
    # Inverted triangles of side s require a base of at least 2s to exist
    # within a larger triangle of side L.
    num_inverted_rows = L - 2 * s + 1
    if num_inverted_rows > 0:
        inverted_count = (num_inverted_rows * (num_inverted_rows + 1)) // 2
    else:
        inverted_count = 0

    total_count = upright_count + inverted_count

    return total_count