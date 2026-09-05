def add_nested_tuples(a, b):
    """
    Perform index wise addition of tuple elements in the given two nested tuples.
    """
    return tuple(sum(x) for x in zip(a, b))