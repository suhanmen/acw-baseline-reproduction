def and_tuples(tuple1, tuple2):
    """
    Extracts the bitwise AND result of elementwise pairs from two tuples.
    """
    result = []
    for a, b in zip(tuple1, tuple2):
        result.append(a & b)
    return tuple(result)