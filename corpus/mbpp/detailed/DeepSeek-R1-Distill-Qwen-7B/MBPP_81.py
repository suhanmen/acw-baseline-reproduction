def zip_tuples(tuple_a, tuple_b):
    """
    Zips two tuples into a list of tuples, element-wise.

    The function takes two tuples as input and returns a list of tuples.
    Each tuple in the output contains corresponding elements from the input tuples.
    If one of the tuples is shorter, the excess elements of the longer tuple are ignored.

    Edge cases:
    - Empty tuple: returns an empty list
    - Single element tuple: returns a list with one tuple
    - All elements in a tuple are equal: returns a list where all tuples are identical
    - Zero or negative numbers: handled as regular numbers
    """
    # Validate inputs
    if not isinstance(tuple_a, tuple) or not isinstance(tuple_b, tuple):
        raise ValueError("Both inputs must be tuples.")

    # Handle empty tuples
    if len(tuple_a) == 0 or len(tuple_b) == 0:
        return []

    # Determine the shorter tuple length
    min_length = min(len(tuple_a), len(tuple_b))

    # Create a list to hold the zipped results
    zipped = []

    # Iterate through each index up to the shorter length
    for i in range(min_length):
        # Append the pair of elements to the zipped list
        zipped.append( (tuple_a[i], tuple_b[i]) )

    # Return the result
    return zipped

# Test cases
assert zip_tuples((7, 8, 4, 5, 9, 10), (1, 5, 6)) == [(7, 1), (8, 5), (4, 6), (5, 1), (9, 5), (10, 6)]
assert zip_tuples((8, 9, 5, 6, 10, 11), (2, 6, 7)) == [(8, 2), (9, 6), (5, 7), (6, 2), (10, 6), (11, 7)]
assert zip_tuples((9, 10, 6, 7, 11, 12), (3, 7, 8)) == [(9, 3), (10, 7), (6, 8), (7, 3), (11, 7), (12, 8)]