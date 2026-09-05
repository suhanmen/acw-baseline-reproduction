def add_nested_tuples(t1, t2):
    """
    Add tuples element-wise from two nested tuples and return the result as a nested tuple.

    Args:
        t1: A nested tuple containing tuples of numbers.
        t2: Another nested tuple containing tuples of numbers.

    Returns:
        A nested tuple where each tuple is the element-wise sum of the corresponding tuples in t1 and t2.

    Raises:
        ValueError: If the input tuples are not of the same structure or contain non-numeric elements.
    """
    # Validate that both inputs are tuples
    if not isinstance(t1, tuple) or not isinstance(t2, tuple):
        raise ValueError("Both inputs must be tuples.")

    # Check if the tuples are empty
    if len(t1) != len(t2):
        raise ValueError("Tuples must be of the same length.")

    # Check each corresponding pair of tuples
    for t1_sub, t2_sub in zip(t1, t2):
        if not isinstance(t1_sub, tuple) or not isinstance(t2_sub, tuple):
            raise ValueError("All elements must be tuples.")
        if len(t1_sub) != len(t2_sub):
            raise ValueError("All corresponding sub-tuples must be of the same length.")
        for a, b in zip(t1_sub, t2_sub):
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise ValueError("All elements must be numeric values.")

    # Perform element-wise addition
    result = []
    for t1_sub, t2_sub in zip(t1, t2):
        sum_sub = tuple(a + b for a, b in zip(t1_sub, t2_sub))
        result.append(sum_sub)

    return tuple(result)