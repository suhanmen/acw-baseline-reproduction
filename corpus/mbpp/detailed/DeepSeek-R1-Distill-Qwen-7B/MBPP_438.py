def count_bidirectional(tuples_list):
    """
    Counts the number of bidirectional tuple pairs in the given list of tuples.

    A bidirectional pair consists of two tuples that are exact reverses of each other.

    Args:
        tuples_list: A list of tuples to be processed.

    Returns:
        int: The number of bidirectional tuple pairs.
    """
    if not tuples_list:
        return 0

    # Convert the list to a set for O(1) lookups
    tuples_set = set(tuples_list)
    bidirectional_pairs = 0

    for tuple in tuples_list:
        # Create the reverse tuple
        reversed_tuple = tuple[::-1]
        # Check if both the tuple and its reverse are present
        if reversed_tuple in tuples_set:
            bidirectional_pairs += 1
            # To avoid double-counting, we can track which tuples we've processed
            tuples_set.remove(tuple)  # This ensures each pair is counted once

    # Since each pair is counted twice (once for each tuple), divide by 2
    return bidirectional_pairs // 2