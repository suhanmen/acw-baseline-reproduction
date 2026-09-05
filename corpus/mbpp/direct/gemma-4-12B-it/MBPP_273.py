def substract_elements(tuple1, tuple2):
    """
    Subtracts the contents of the second tuple from the first tuple 
    using corresponding indices.
    """
    return tuple(a - b for a, b in zip(tuple1, tuple2))