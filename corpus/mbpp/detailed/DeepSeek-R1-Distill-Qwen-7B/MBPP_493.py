import math

def calculate_polygons(rows, cols, x_start, y_start, offset, size):
    """
    Calculate a grid of hexagon coordinates.

    Args:
        rows (int): Number of rows in the hexagon grid.
        cols (int): Number of columns in the hexagon grid.
        x_start (int): Starting x-coordinate for the grid.
        y_start (int): Starting y-coordinate for the grid.
        offset (int): Offset for the grid arrangement.
        size (int): Size of each hexagon.

    Returns:
        list: A list of lists containing tuples of x, y coordinates for each hexagon.
    """
    # Validate inputs
    if not (isinstance(rows, int) and isinstance(cols, int) and
            isinstance(x_start, int) and isinstance(y_start, int) and
            isinstance(offset, int) and isinstance(size, int)):
        raise AssertionError("All input values must be integers.")
    if rows < 0 or cols < 0 or x_start < 0 or y_start < 0 or offset < 0 or size < 0:
        raise AssertionError("All input values must be non-negative.")

    # Calculate hexagon dimensions
    width = 2 * size + offset
    height = math.sqrt(3) * size + (size * math.sqrt(3)) // 2 + offset

    # Helper function to convert axial to cartesian coordinates
    def axial_to_cartesian(axial_coords, size, offset, y_start):
        (q, r) = axial_coords
        x = q + r * 0.5
        y = (r * math.sqrt(3) // 2) + y_start
        return (x * width + x_start, y * height + y_start + offset * y_start)

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            # Calculate axial coordinates
            axial = (i, j)
            coord = axial_to_cartesian(axial, size, offset, y_start)
            row.append(coord)
        result.append([round(coord[0], 10), round(coord[1], 10)] for coord in row)

    return result

# Example assertions ( uncomment and adjust according to test cases )
# assert calculate_polygons(1,1,4,4,3)==[[(-5.0, -4.196152422706632), (-5.0, -0.7320508075688767), (-2.0, 1.0), (1.0, -0.7320508075688767), (1.0, -4.196152422706632), (-2.0, -5.928203230275509), (-5.0, -4.196152422706632)], [(1.0, -4.196152422706632), (1.0, -0.7320508075688767), (4.0, 1.0), (7.0, -0.7320508075688767), (7.0, -4.196152422706632), (4.0, -5.928203230275509), (1.0, -4.196152422706632)], [(7.0, -4.196152422706632), (7.0, -0.7320508075688767), (10.0, 1.0), (13.0, -0.7320508075688767), (13.0, -4.196152422706632), (10.0, -5.928203230275509), (7.0, -4.196152422706632)], [(-2.0, 1.0000000000000004), (-2.0, 4.464101615137755), (1.0, 6.196152422706632), (4.0, 4.464101615137755), (4.0, 1.0000000000000004), (1.0, -0.7320508075688767), (-2.0, 1.0000000000000004)], [(4.0, 1.0000000000000004), (4.0, 4.464101615137755), (7.0, 6.196152422706632), (10.0, 4.464101615137755), (10.0, 1.0000000000000004), (7.0, -0.7320508075688767), (4.0, 1.0000000000000004)], [(-5.0, 6.196152422706632), (-5.0, 9.660254037844387), (-2.0, 11.392304845413264), (1.0, 9.660254037844387), (1.0, 6.196152422706632), (-2.0, 4.464101615137755), (-5.0, 6.196152422706632)], [(1.0, 6.196152422706632), (1.0, 9.660254037844387), (4.0, 11.392304845413264), (7.0, 9.660254037844387), (7.0, 6.196152422706632), (4.0, 4.464101615137755), (1.0, 6.196152422706632)], [(4.0, 11.392304845413264), (4.0, 14.856406460551023), (7.0, 16.588457268119896), (10.0, 14.856406460551023), (10.0, 11.392304845413264), (7.0, 9.660254037844387), (4.0, 11.392304845413264)], [(-3.0, 4.0), (-3.0, 13.237604307034012), (5.0, 17.856406460551018), (13.0, 13.237604307034012), (13.0, 4.0), (5.0, -0.6188021535170058), (-3.0, 4.0)], [(13.0, 4.0), (13.0, 13.237604307034012), (21.0, 17.856406460551018), (29.0, 13.237604307034012), (29.0, 4.0), (21.0, -0.6188021535170058), (13.0, 4.0)], [(-11.0, 17.856406460551018), (-11.0, 27.09401076758503), (-3.0, 31.712812921102035), (5.0, 27.09401076758503), (5.0, 17.856406460551018), (-3.0, 13.237604307034012), (-11.0, 17.856406460551018)], [(5.0, 17.856406460551018