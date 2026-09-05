def find_exponentio(tuple1, tuple2):
    """
    Performs element-wise exponentiation of two tuples.
    The first tuple contains the bases, and the second tuple contains the exponents.
    """
    return tuple(base ** exponent for base, exponent in zip(tuple1, tuple2))