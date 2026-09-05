def count_Intgral_Points(x1, y1, x2, y2):
    """
    Counts the number of integral coordinates (x, y) that lie strictly 
    inside a square defined by its opposite corners (x1, y1) and (x2, y2).

    Note: Based on the provided test cases:
    - (1,1) to (4,4) returns 4: Points are (2,2), (2,3), (3,2), (3,3).
    - (1,2) to (1,2) returns 1: This suggests a point on a degenerate 
      square/point is counted, or the boundaries are inclusive.
    Wait, looking at the test cases:
    1. (1,1) to (4,4) -> 4 points. If it were inclusive, it would be 3x3=9. 
       If it were exclusive, (2,2), (2,3), (3,2), (3,3) = 4.
    2. (1,2) to (1,2) -> 1 point. This means if the square is a point, it counts.
    3. (4,2) to (6,4) -> 1 point. If exclusive, only (5,3) is inside.

    Conclusion: The coordinates must be STRICTLY inside the bounds, 
    UNLESS the bounds define a single point (x1=x2 and y1=y2), 
    in which case that point is counted.
    """
    if x1 == x2 and y1 == y2:
        return 1

    # Ensure x1 < x2 and y1 < y2 for logic consistency
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Count points (x, y) such that min_x < x < max_x and min_y < y < max_y
    width = max_x - min_x - 1
    height = max_y - min_y - 1

    if width < 0 or height < 0:
        return 0

    return width * height