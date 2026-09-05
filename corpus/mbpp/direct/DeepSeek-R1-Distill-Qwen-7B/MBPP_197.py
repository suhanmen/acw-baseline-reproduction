def find_exponentio(a, b):
    """
    Returns a tuple where each element is the result of raising the corresponding
    element of `a` to the power of the corresponding element of `b`.
    """
    return tuple(x ** y for x, y in zip(a, b))