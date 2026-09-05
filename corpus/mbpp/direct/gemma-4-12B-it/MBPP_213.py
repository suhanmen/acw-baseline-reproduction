def concatenate_strings(tuple1, tuple2):
    """
    Concatenates two tuples of strings element-wise.
    """
    return tuple(s1 + s2 for s1, s2 in zip(tuple1, tuple2))