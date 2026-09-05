def median_trapezium(a, b, c):
    """
    Finds the median of a trapezium.
    In the context of the provided test cases:
    median_trapezium(15, 25, 35) -> (15 + 35) / 2 = 25 (Wait, the assertion says 20)
    Looking at the pattern:
    (15 + 25) / 2 = 20
    (10 + 20) / 2 = 15
    (6 + 9) / 2 = 7.5

    The median of a trapezium with parallel sides a and b is the average of those sides.
    The third parameter 'c' represents the height or a side that doesn't affect 
    the length of the median line segment parallel to the bases.
    """
    return (a + b) / 2