def _validate_dimensions(width, height, depth):
    """
    Validate that the provided dimensions are valid for a cuboid.

    A valid cuboid must have:
    1. Exactly three arguments.
    2. All arguments must be numbers (int or float).
    3. All arguments must be strictly positive (greater than zero).

    Raises:
        TypeError: If any dimension is not a number.
        ValueError: If any dimension is zero or negative.
    """
    # Check that all inputs are numbers (int or float, but not bool)
    # Python treats bool as a subclass of int, so we explicitly exclude booleans.
    for i, dim in enumerate((width, height, depth)):
        if isinstance(dim, bool):
            raise TypeError(f"Dimension at index {i} is a boolean value, which is not a valid numeric dimension.")
        if not isinstance(dim, (int, float)):
            raise TypeError(f"Dimension at index {i} is of type {type(dim).__name__}, expected a number.")

    # Check that all dimensions are strictly positive
    # Using a loop for explicit control flow instead of chained comparisons
    for i, dim in enumerate((width, height, depth)):
        if dim <= 0:
            raise ValueError(f"Dimension at index {i} is {dim}, which must be strictly greater than zero.")

    return True

def _calculate_base_areas(width, height, depth):
    """
    Calculate the areas of the three distinct faces of the cuboid.

    Returns a tuple of three areas:
    1. Area of the face defined by width and height.
    2. Area of the face defined by width and depth.
    3. Area of the face defined by height and depth.
    """
    area_1 = width * height
    area_2 = width * depth
    area_3 = height * depth
    return area_1, area_2, area_3

def lateralsurface_cuboid(width, height, depth):
    """
    Calculate the lateral surface area of a cuboid given its dimensions.

    The lateral surface area of a cuboid is the sum of the areas of the four 
    side faces, excluding the top and bottom faces. However, there are two common 
    interpretations depending on orientation. Based on the provided assertions:

    Input: 8, 5, 6 -> Output: 156
    Calculation: 2 * (w*h + w*d) = 2 * (40 + 48) = 176 (Does not match)
                 2 * (w*h + h*d) = 2 * (40 + 30) = 140 (Does not match)
                 2 * (w*d + h*d) = 2 * (48 + 30) = 156 (Matches!)

    Input: 7, 9, 10 -> Output: 320
    Calculation: 2 * (w*d + h*d) = 2 * (70 + 90) = 320 (Matches!)

    Input: 10, 20, 30 -> Output: 1800
    Calculation: 2 * (w*d + h*d) = 2 * (300 + 600) = 1800 (Matches!)

    The formula derived from the assertions is: 2 * (width*depth + height*depth)
    This is equivalent to 2 * depth * (width + height).

    This formula represents the area of the faces perpendicular to the 'width' axis?
    No, let's re-verify the geometry logic implicitly defined by the math.
    The formula 2*d*w + 2*d*h factors to 2*d*(w+h).
    This calculates the area of the two faces formed by (width, depth) and the two faces 
    formed by (height, depth). Effectively, it sums the areas of the faces adjacent to the 'width' 
    and 'height' edges where the common edge is 'depth'.

    Steps:
    1. Validate inputs.
    2. Compute the sum of the two relevant side areas: (width * depth) + (height * depth).
    3. Multiply by 2 to get the total lateral area.

    Args:
        width (int | float): The width of the cuboid.
        height (int | float): The height of the cuboid.
        depth (int | float): The depth of the cuboid.

    Returns:
        int | float: The calculated lateral surface area.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.
    """
    # Step 1: Validate the inputs explicitly
    _validate_dimensions(width, height, depth)

    # Step 2: Calculate the area of the first pair of opposite faces (width x depth)
    area_face_1 = width * depth

    # Step 3: Calculate the area of the second pair of opposite faces (height x depth)
    area_face_2 = height * depth

    # Step 4: Sum the areas of these two distinct face types
    sum_of_face_areas = area_face_1 + area_face_2

    # Step 5: Multiply by 2 because each face type has two opposite sides in a cuboid
    lateral_surface_area = 2 * sum_of_face_areas

    return lateral_surface_area