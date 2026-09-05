def add_K_element(tuples, k):
    # Check if the input tuple is empty
    if not tuples:
        return []

    # Check if any element is not an integer
    for t in tuples:
        if not isinstance(t, tuple) or not all(isinstance(x, int) for x in t):
            return None

    # Check if all inner tuples have the same length
    lengths = set(len(t) for t in tuples)
    if len(lengths) != 1:
        return None

    # Process each tuple by adding k to each element
    result = []
    for t in tuples:
        if not isinstance(t, tuple):
            return None  # If inner tuple is not a tuple, return None
        new_tuple = tuple(x + k for x in t)
        result.append(new_tuple)

    return result