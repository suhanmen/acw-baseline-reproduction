def division_elements(tuple1, tuple2):
    """
    Performs element-wise integer division on two tuples.

    Args:
        tuple1 (tuple): The numerator tuple.
        tuple2 (tuple): The denominator tuple.

    Returns:
        tuple: The result of element-wise integer division.
    """
    return tuple(a // b for a, b in zip(tuple1, tuple2))