import math

def calculate_polygons(rows, cols, width, height, radius):
    """
    Calculate a grid of hexagon coordinates.

    Args:
        rows: Number of rows (vertical count of hexagons)
        cols: Number of columns (horizontal count of hexagons)
        width: Width of the entire grid (in coordinate units)
        height: Height of the entire grid (in coordinate units)
        radius: Radius of each hexagon

    Returns:
        A list of lists, where each inner list contains 7 tuples (the 6 vertices + first vertex repeated).
    """
    result = []

    # Calculate scaling factors based on the grid dimensions and the provided width/height
    # The problem implies a regular hexagonal grid. We need to map the logical grid to the given width/height.
    # Based on the examples, the hexagons are "pointy topped".
    # The distance between centers horizontally is 2*radius.
    # The distance between centers vertically is sqrt(3)*radius.

    # However, the examples show specific coordinates that match a specific pattern.
    # Let's derive the pattern from the first example: calculate_polygons(1,1, 4, 4, 3)
    # Radius = 3. Width = 4, Height = 4.
    # The center of the single hexagon seems to be around (1, 0).
    # Vertices: (-5.0, -4.196...), (-5.0, -0.732...), (-2.0, 1.0), (1.0, -0.732...), (1.0, -4.196...), (-2.0, -5.928...)
    # Let's analyze the vertices relative to a center (cx, cy).
    # For a pointy-top hexagon with radius R=3:
    # Vertices are at angles: 0, 60, 120, 180, 240, 300? Or rotated?
    # The vertices in the example look like:
    # Top-Left: (-5, -4.196), Top: (-5, -0.732) ? No, let's look at the structure.
    # Actually, the vertices are listed in clockwise or counter-clockwise order.
    # Let's assume the hexagon is defined by a center (cx, cy).
    # The vertices given for the first hexagon in example 1:
    # (-5.0, -4.196152422706632)
    # (-5.0, -0.7320508075688767)
    # (-2.0, 1.0)
    # (1.0, -0.7320508075688767)
    # (1.0, -4.196152422706632)
    # (-2.0, -5.928203230275509)
    # Closing back to (-5.0, -4.196152422706632)

    # Let's try to fit a center (cx, cy).
    # Average X: (-5-5-2+1+1-2)/6 = -11/6 = -1.833?
    # Average Y: (-4.196-0.732+1-0.732-4.196-5.928)/6 = -16.78/6 = -2.8?
    # This seems messy. Let's look at the relative distances.
    # Vector from (-5, -4.196) to (-2, -5.928) is (3, -1.732). Length = sqrt(9 + 3) = sqrt(12) = 2*sqrt(3) ~ 3.464.
    # If radius is 3, the distance from center to vertex is 3.
    # Maybe the "radius" parameter is actually the distance from center to edge (apothem)? No, "radius" usually means center to vertex.
    # Let's check the distance between (-5, -4.196) and (-5, -0.732). It's 3.464.
    # Wait, the first two points are (-5, -4.196) and (-5, -0.732). The distance is 3.464.
    # If R=3, then side length a = R = 3. Distance between adjacent vertices is 3.
    # Here distance is 3.464 = 2*sqrt(3). This is the distance between two vertices separated by one vertex (i.e., skipping one).
    # So the hexagon side length 'a' might be related to R differently, or R is the side length?
    # If R=3 is the side length, then vertices are at distance 3 from each other.
    # But the distance between (-5, -4.196) and (-5, -0.732) is 3.464. That's not 3.
    # Perhaps the hexagon is rotated?
    # Let's re-examine the coordinates.
    # Maybe the function generates the grid based on a specific coordinate system logic.

    # Let's try to reverse engineer the grid generation logic from the example data directly.
    # Example 1: 1 row, 1 col.
    # Example 2: 5 rows, 4 cols, width=7, height=9, radius=8.
    # The output has 5 rows of hexagons.
    # Row 0: 3 hexagons? No, the list has 10 elements (5 rows * 2 cols?).
    # Wait, the output list length for (5,4) is 10. So it's 5 rows and 2 columns?
    # But the input says cols=4.
    # Let's count the inner lists in example 2 output:
    # It has 10 lists.
    # Row 0: 3 items?
    # Let's look at the first few X coordinates in Example 2:
    # Row 0 (index 0): -11, -11, -3, 5, 5, -3. Center X approx (-3 + 5)/2 = 1? Or (-3-3)/2 = -3?
    # Let's trace the centers.
    # Hexagon 0: X range -11 to 5. Center approx -3.
    # Hexagon 1: X range 5 to 21. Center approx 13.
    # Hexagon 2: X range 21 to 29. Center approx 25?
    # Wait, the output is a list of lists.
    # List 0: Center approx (-3, something).
    # List 1: Center approx (13, something).
    # List 2: Center approx (25, something).
    # List 3: Center approx (-3, something else).
    # So it looks like a 3x3 grid? But input is (5, 4).
    # Let's re-read the assertion carefully.
    # assert calculate_polygons(5,4,7,9,8) == ...
    # The output has 10 items. 5 rows * 2 cols? Or 10 items total?
    # If cols=4, we expect 4 columns. If rows=5, we expect 5 rows. Total 20 hexagons.
    # But the output has only 10 lists.
    # Maybe the function generates a bounding box of hexagons that fits within width/height?
    # Or maybe the "cols" and "rows" arguments mean something else?
    # Let's check the output of example 1 again: (1,1,4,4,3). Output has 1 list. Correct.
    # Example 3: (9,6,4,3,2). Output has 2 lists.
    # Input: rows=9, cols=6. Output: 2 lists.
    # This suggests the number of items returned is NOT rows*cols.
    # It seems to be related to fitting hexagons into the specified width and height.
    # Let's deduce the grid density.

    # Hypothesis: The function calculates how many hexagons fit in the given width and height, starting from a top-left alignment, but the arguments (rows, cols) might be ignored or used differently?
    # NO, the problem statement says "function returns a list of lists containing 6 tuples...".
    # And the first two arguments are likely dimensions of the grid (rows, cols).
    # But why does (5,4) produce 10 hexagons?
    # 5 rows * 4 cols = 20.
    # Unless... it's a specific shape? Or maybe I am miscounting the output lists.
    # Let's count the commas separating the outer lists in the string representation of the assertion.
    # Actually, I can count the opening brackets `[`.
    # Example 2 output:
    # [[...], [...], [...], [...], [...], [...], [...], [...], [...], [...]] -> 10 lists.
    # So it's a grid of 2 columns and 5 rows?
    # Input was (5, 4). So rows=5, cols=4? But output has 2 cols.
    # Maybe the arguments are (height, width) in terms of number of hexagons? No, 5 rows, 2 cols.
    # Is it possible the input (rows, cols) defines the bounds, and the function calculates the hexagons inside?
    # Or maybe the arguments are (start_row, start_col, width, height)? No, 3rd and 4th are width and height.
    # Let's look at the X coordinates again for Example 2.
    # List 0: X min -11, X max 5. Width 16.
    # List 1: X min 5, X max 21. Width 16.
    # List 2: X min 21, X max 29. Width 8? Wait.
    # List 2: (21.0, -9.85...), (21.0, -0.61...), (29.0, 4.0), (37.0, -0.61...), (37.0, -9.85...), (29.0, -14.47...)
    # X range 21 to 37. Width 16.
    # List 3: X range -3 to 13. Width 16.
    # So the horizontal step is 8 (center to center)?
    # Center of List 0: (-11+5)/2 = -3.
    # Center of List 1: (5+21)/2 = 13.
    # Center of List 2: (21+37)/2 = 29.
    # Center of List 3: (-3+13)/2 = 5.
    # So centers are: -3, 13, 29, -3, 5... wait, List 4 (index 3) is (-3, 13, 29...), List 3 (index 2) is 21..37.
    # Let's list the center X of the first 4 items:
    # Item 0: -3
    # Item 1: 13
    # Item 2: 29
    # Item 3: -3 ?? No, Item 3 is [(-3.0, 4.0), ...]. Center X = (-3+13)/2 = 5.
    # Item 4: [(13.0, 4.0)...]. Center X = (13+29)/2 = 21.
    # Item 5: [(-11.0, 17.85...)]. Center X = -3.
    # Item 6: [(5.0, 17.85...)]. Center X = 13? (5+21)/2 = 13.
    # Item 7: [(21.0, 17.85...)]. Center X = 29.
    # Item 8: [(-3.0, 31.71...)]. Center X = 5.
    # Item 9: [(13.0, 31.71...)]. Center X = 21.

    # Grid of centers (x, y):
    # Row 0: -3, 13, 29 ... (Wait, only 3 items in row 0?)
    # Row 1: -3, 13, 29 (Indices 3,4,5? No, indices 3,4,5 are row 1? No.)
    # The output is a flat list of hexagons.
    # Let's re-group by Y coordinate (approx).
    # Y centers:
    #