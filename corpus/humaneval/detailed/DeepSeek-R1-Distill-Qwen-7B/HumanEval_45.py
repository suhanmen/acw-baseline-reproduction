def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Handle case where inputs are not numbers
    try:
        a_num = float(a)
        h_num = float(h)
    except ValueError:
        return None

    # Check if a or h is less than or equal to zero
    if a_num <= 0 or h_num <= 0:
        return None

    # Calculate the area
    area = (a_num * h_num) / 2

    return area