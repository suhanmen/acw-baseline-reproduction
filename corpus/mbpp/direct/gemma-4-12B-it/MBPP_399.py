def bitwise_xor(tuple1, tuple2):
    """
    Perform the mathematical bitwise xor operation across two tuples.

    Args:
        tuple1 (tuple): First tuple of integers.
        tuple2 (tuple): Second tuple of integers.

    Returns:
        tuple: A tuple containing the bitwise XOR results.
    """
    return tuple(a ^ b for a, b in zip(tuple1, tuple2))