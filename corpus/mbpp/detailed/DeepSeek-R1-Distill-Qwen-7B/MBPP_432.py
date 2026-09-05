def median_trapezium(a, b):
    """
    Calculate the median of a trapezium.

    The median of a trapezium is the line segment connecting the midpoints of the non-parallel sides.
    Its length is the average of the lengths of the two parallel sides.

    Args:
        a (int/float): Length of the first parallel side.
        b (int/float): Length of the second parallel side.

    Returns:
        float: The length of the median.
    """
    median = (a + b) / 2
    return median