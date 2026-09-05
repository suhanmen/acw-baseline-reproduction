def count_Intgral_Points(x1, y1, x2, y2):
    """
    Count the number of integral coordinates that lie strictly inside a square defined by
    two opposite corners (x1, y1) and (x2, y2).

    The function interprets the square as the region between the minimum and maximum
    x-coordinates and the minimum and maximum y-coordinates of the given points.
    Points lying exactly on the boundary of the square are NOT counted as "inside".
    Only points with integer coordinates strictly within the bounds are counted.

    Parameters:
    x1, y1, x2, y2 (int or float): Coordinates of two opposite corners of the square.

    Returns:
    int: The number of integral coordinates strictly inside the square.

    Raises:
    TypeError: If any input is not a number.
    ValueError: If the coordinates are not finite, or if the square is degenerate (points are identical).
    """

    # Step 1: Input Validation - Type Checking
    required_types = (int, float)

    if not isinstance(x1, required_types):
        raise TypeError(f"x1 must be a number, got {type(x1).__name__}")
    if not isinstance(y1, required_types):
        raise TypeError(f"y1 must be a number, got {type(y1).__name__}")
    if not isinstance(x2, required_types):
        raise TypeError(f"x2 must be a number, got {type(x2).__name__}")
    if not isinstance(y2, required_types):
        raise TypeError(f"y2 must be a number, got {type(y2).__name__}")

    # Step 2: Input Validation - Finiteness Check
    import math

    if not math.isfinite(x1):
        raise ValueError("x1 must be a finite number")
    if not math.isfinite(y1):
        raise ValueError("y1 must be a finite number")
    if not math.isfinite(x2):
        raise ValueError("x2 must be a finite number")
    if not math.isfinite(y2):
        raise ValueError("y2 must be a finite number")

    # Step 3: Normalize Coordinates to handle arbitrary ordering of inputs
    # Determine the minimum and maximum for both x and y axes to define the square boundaries.
    x_min = float(x1) if x1 < x2 else float(x2)
    x_max = float(x1) if x1 > x2 else float(x2)

    y_min = float(y1) if y1 < y2 else float(y2)
    y_max = float(y1) if y1 > y2 else float(y2)

    # Step 4: Check for Degenerate Cases
    # If the start and end points are the same, the area is zero, so no points inside.
    if x_min == x_max or y_min == y_max:
        return 0

    # Step 5: Determine Strict Interior Bounds
    # A point (x, y) is inside if x_min < x < x_max and y_min < y < y_max.
    # Since we are looking for integers:

    # The smallest integer strictly greater than x_min
    lower_x_bound = int(math.floor(x_min)) + 1

    # The largest integer strictly less than x_max
    upper_x_bound = int(math.ceil(x_max)) - 1

    # The smallest integer strictly greater than y_min
    lower_y_bound = int(math.floor(y_min)) + 1

    # The largest integer strictly less than y_max
    upper_y_bound = int(math.ceil(y_max)) - 1

    # Step 6: Handle Cases where No Integers Exist in the Range
    # If lower_bound >= upper_bound for any axis, there are no integers in that dimension.
    count_x = 0
    if lower_x_bound <= upper_x_bound:
        count_x = upper_x_bound - lower_x_bound + 1

    count_y = 0
    if lower_y_bound <= upper_y_bound:
        count_y = upper_y_bound - lower_y_bound + 1

    # Step 7: Calculate Total Points
    # The total number of points is the product of the count of valid x-coordinates
    # and the count of valid y-coordinates.
    total_points = count_x * count_y

    return int(total_points)