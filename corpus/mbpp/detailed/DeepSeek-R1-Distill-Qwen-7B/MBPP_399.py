def bitwise_xor(tuple_a, tuple_b):
    """
    Perform a bitwise XOR operation across two tuples of integers.

    Args:
        tuple_a (tuple): A tuple of integers.
        tuple_b (tuple): Another tuple of integers with the same length as tuple_a.

    Returns:
        tuple: A tuple where each element is the result of the bitwise XOR
              operation between the corresponding elements of tuple_a and tuple_b.

    Raises:
        ValueError: If the inputs are not tuples of the same length.
    """
    # Validate inputs
    if not isinstance(tuple_a, tuple) or not isinstance(tuple_b, tuple):
        raise ValueError("Both inputs must be tuples.")

    # Check if tuples are of the same length
    if len(tuple_a) != len(tuple_b):
        raise ValueError("Tuples must be of the same length.")

    # Handle empty tuples
    if len(tuple_a) == 0:
        return ()

    # Perform bitwise XOR operation element-wise
    result = []
    for a, b in zip(tuple_a, tuple_b):
        result.append(a ^ b)

    return tuple(result)