import math
from typing import List, Tuple, Optional, Any, Union

def _validate_hex_grid_input(
    columns: Any,
    rows: Any,
    x_spacing: Any,
    y_spacing: Any,
    width_units: Any
) -> None:
    """
    Validates the input arguments for the hex grid generation.

    Requirements:
    - columns: Integer number of columns.
    - rows: Integer number of rows.
    - x_spacing: Positive numeric value representing horizontal distance between centers.
    - y_spacing: Positive numeric value representing vertical distance between centers.
    - width_units: Positive numeric value representing the horizontal width of the hex.

    Raises ValueError if any argument is invalid.
    """

    # Check for None values
    if columns is None or rows is None or x_spacing is None or y_spacing is None or width_units is None:
        raise ValueError("All arguments must be non-None.")

    # Check types
    if not isinstance(columns, int):
        raise TypeError("The 'columns' argument must be an integer.")
    if not isinstance(rows, int):
        raise TypeError("The 'rows' argument must be an integer.")
    if not isinstance(x_spacing, (int, float)):
        raise TypeError("The 'x_spacing' argument must be a number (int or float).")
    if not isinstance(y_spacing, (int, float)):
        raise TypeError("The 'y_spacing' argument must be a number (int or float).")
    if not isinstance(width_units, (int, float)):
        raise TypeError("The 'width_units' argument must be a number (int or float).")

    # Check for zero or negative values
    if columns < 0:
        raise ValueError("The 'columns' argument must be non-negative.")
    if rows < 0:
        raise ValueError("The 'rows' argument must be non-negative.")
    if x_spacing <= 0:
        raise ValueError("The 'x_spacing' argument must be positive.")
    if y_spacing <= 0:
        raise ValueError("The 'y_spacing' argument must be positive.")
    if width_units <= 0:
        raise ValueError("The 'width_units' argument must be positive.")


def _calculate_apothem(width_units: float) -> float:
    """
    Calculates the apothem of a regular hexagon given its width (flat-to-flat distance).

    The apothem is the distance from the center to the midpoint of a side.
    For a hexagon with flat-to-flat width W:
    Apothem = W * cos(30 degrees) = W * sqrt(3) / 2

    Parameters:
    - width_units: The width of the hexagon (distance between parallel sides).

    Returns:
    - The apothem as a float.
    """
    sqrt_3 = math.sqrt(3.0)
    apothem = width_units * (sqrt_3 / 2.0)
    return apothem


def _generate_single_hexagon_coordinates(
    col: int,
    row: int,
    x_spacing: float,
    y_spacing: float,
    width_units: float
) -> List[Tuple[float, float]]:
    """
    Generates the 7 vertex coordinates for a single hexagon at the given grid position.

    This function handles the offset layout for hexagonal grids.
    In a 'pointy-topped' hex grid:
    - Even columns are shifted down.
    - Odd columns are shifted up.
    - Alternatively, rows can be offset. The example output suggests a specific offset pattern.

    Analysis of the first example output (1,1, 4, 4, 3):
    Center of hex at col=0, row=0 appears to be roughly (-1.0, -2.436...)?
    Actually, let's deduce the center from the vertices.
    Vertices for first hex:
    (-5.0, -4.196...)
    (-5.0, -0.732...)
    (-2.0, 1.0)
    ...

    Let's look at the shape. It's a flat-top hexagon rotated? Or pointy-top?
    The vertices have x coordinates: -5.0, -5.0, -2.0, 1.0, 1.0, -2.0.
    Width = -2.0 - (-5.0) * 2 ? No.
    Max X = 1.0, Min X = -5.0. Range = 6.0.
    If width_units = 3 (given in input), then flat-to-flat distance is 3.
    But here range is 6.0. This implies the hexagon is rotated or the width_units parameter means something else,
    OR the hexagon is defined differently.

    Wait, let's re-examine the input: `calculate_polygons(1,1, 4, 4, 3)`.
    Usually arguments are (rows, cols, width, height, scale) or similar.
    Here: 1 col, 1 row. x_spacing=4, y_spacing=4, width_units=3.
    The hexagon width is 6.0?
    If width_units=3, and the hexagon spans 6.0 in X, maybe width_units is the radius?
    If radius = 3, then diameter = 6. This matches.
    Let's assume `width_units` is the circumradius (distance from center to vertex).

    If radius R = 3:
    Vertices on a circle of radius 3.
    Standard angles for pointy-top hex (pointing up/down):
    0, 60, 120, 180, 240, 300.
    Or for flat-top: 30, 90, 150, 210, 270, 330.

    Let's test Pointy-Top (points at N/S):
    Angles: 90, 30, -30, -90, -150, 150 (relative to x-axis).
    X = R * cos(theta), Y = R * sin(theta).
    If we align such that the "top" is flat?
    The example shows horizontal sides?
    Vertices: (-5, -4.19), (-5, -0.73), (-2, 1), (1, -0.73), (1, -4.19), (-2, -5.92).
    Side 1: (-5, -4.19) to (-5, -0.73). Vertical line? Length ~ 3.46.
    Side 2: (-5, -0.73) to (-2, 1). dx=3, dy=1.73. Length sqrt(9+3)=3.46.
    Side 3: (-2, 1) to (1, -0.73). dx=3, dy=-1.73.
    Side 4: (1, -0.73) to (1, -4.19). Vertical line.
    Side 5: (1, -4.19) to (-2, -5.92).
    Side 6: (-2, -5.92) to (-5, -4.19).

    This hexagon has two vertical sides. This is a "Flat-Top" hexagon if we consider the standard orientation where "flat" means horizontal, BUT here the flat sides are vertical.
    Actually, if the sides are vertical, it's a hexagon rotated 90 degrees from the usual "flat-top" (which has horizontal tops).
    Usually:
    Flat-top: Top/Bottom sides are horizontal. Left/Right vertices are points.
    Pointy-top: Left/Right sides are vertical. Top/Bottom vertices are points.

    The example has vertical sides. So it looks like a "Pointy-Top" hexagon where the points are at Top and Bottom?
    No, if points are Top/Bottom, the sides connecting them are slanted.
    If sides are vertical, the points must be Left and Right.
    Left point: (-5, -2.46)?
    Right point: (1, -2.46)?
    Width (point-to-point) = 6.0.
    This matches `width_units` = 3 being the radius (distance from center to vertex).
    Center X = (-5 + 1) / 2 = -2.0.
    Center Y = (-2.46...)? 
    Let's calculate center from average of vertices:
    X_sum = -5-5-2+1+1-2 = -12. Avg = -2.0.
    Y_sum = -4.196 -0.732 +1 -0.732 -4.196 -5.928 = -14.784. Avg = -2.464.
    Center = (-2.0, -2.464).

    Now let's check the offsets.
    The hex grid seems to be arranged such that:
    Column 0: Center X = -2.0.
    Column 1 (from example 2): Center X = 1.0.
    Difference = 3.0.
    Given `x_spacing` = 4.
    So Col 0: X = -2.0.
    Col 1: X = 1.0.
    Formula: X_center = (Col * x_spacing) - 2.0 ?
    Col 0: -2.0.
    Col 1: 4 - 2 = 2.0 (Wait, example 2 starts with 1.0).

    Let's re-read the example 2:
    `calculate_polygons(5,4,7,9,8)`
    First hex in first row, first col:
    Vertex list starts: (-11.0, ...), (-11.0, ...), (-3.0, 4.0)...
    Center X = (-11 + -3 + ...)/7.
    Min X = -11, Max X = 5. Range = 16.
    Radius = 8.0.
    Given `width_units` = 8.
    Matches: `width_units` is the circumradius.
    Center X for first hex: (-11 + 5) / 2 = -3.0?
    Wait, vertices: (-11, -9.85), (-11, -0.61), (-3, 4), (5, -0.61), (5, -9.85), (-3, -14.47).
    X coords: -11, -11, -3, 5, 5, -3.
    Center X = (-11 -11 -3 + 5 + 5 -3) / 6 = -18 / 6 = -3.0.
    Given `x_spacing` = 7.
    If Col 0 -> -3.0.
    Col 1 (second hex in first row): (5, -9.85)...
    X coords: 5, 5, 13, 21, 21, 13.
    Center X = (5+5+13+21+21+13)/6 = 78/6 = 13.0.
    Difference = 13.0 - (-3.0) = 16.0.
    But `x_spacing` is 7.
    Something is wrong with my assumption about the layout or the formula.

    Let's look at the second assertion again: `calculate_polygons(5,4,7,9,8)`.
    Input: rows=5, cols=4, x_spacing=7, y_spacing=9, width_units=8.
    Output has 10 hexagons.
    Row 0: 3 hexagons?
    Row 1: 3 hexagons?
    Row 2: 3 hexagons?
    Wait, the output list length is 10.
    The structure of the output list of lists:
    [[hex0], [hex1], [hex2], [hex3], [hex4], [hex5], [hex6], [hex7], [hex8], [hex9]]
    But the example input says `calculate_polygons(5,4,...)`.
    Usually (rows, cols). 5 rows, 4 cols = 20 hexagons.
    Why are there only 10?
    Maybe the arguments are (cols, rows)?
    If cols=5, rows=4. Total 20. Still 10.

    Let's count the hexagons in the provided output for the second case.
    1. [(-11, ...), ...]
    2. [(5, ...), ...]
    3. [(21, ...), ...]
    4. [(-3, 4), ...]
    5. [(13, 4), ...]
    6. [(-11, 17), ...]
    7. [(5, 17), ...]
    8. [(21, 17), ...]
    9. [(-3, 31