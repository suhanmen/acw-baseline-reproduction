def find_exponentio(base_tuple, exponent_tuple):
    """
    Perform element-wise exponentiation of two tuples.

    Args:
        base_tuple (tuple of int): The base elements for exponentiation.
        exponent_tuple (tuple of int): The exponent elements for exponentiation.

    Returns:
        tuple of int: A tuple where each element is the result of raising the corresponding
                      element of base_tuple to the power of the corresponding element
                      in exponent_tuple.
    """
    # Handle the case where either tuple is empty
    if not base_tuple or not exponent_tuple or len(base_tuple) != len(exponent_tuple):
        return ()

    # Perform element-wise exponentiation
    result = ()
    for base, exp in zip(base_tuple, exponent_tuple):
        result += (base ** exp,)

    return result

# Test the function with the provided examples
print(find_exponentio((10, 4, 5, 6), (5, 6, 7, 5)))  # Expected: (100000, 4096, 78125, 7776)
print(find_exponentio((11, 5, 6, 7), (6, 7, 8, 6)))  # Expected: (1771561, 78125, 1679616, 117649)
print(find_exponentio((12, 6, 7, 8), (7, 8, 9, 7)))  # Expected: (35831808, 1679616, 40353607, 2097152)