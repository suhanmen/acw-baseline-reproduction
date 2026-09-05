def get_equal(tuples_list):
    # Validate input: must be a list of tuples
    if not isinstance(tuples_list, list):
        return 'Invalid input'

    # Check if all elements in the list are tuples
    for item in tuples_list:
        if not isinstance(item, tuple):
            return 'Invalid input'

    # Case: empty list of tuples
    if len(tuples_list) == 0:
        return 'All tuples have same length'

    # Determine the expected length from the first tuple
    first_tuple = tuples_list[0]
    expected_length = len(first_tuple)

    # Case: first tuple is empty
    if expected_length == 0:
        for tuple_ in tuples_list:
            if len(tuple_) != 0:
                return 'All tuples do not have same length'
        return 'All tuples have same length'

    # Get all tuple lengths
    tuple_lengths = [len(t) for t in tuples_list]

    # Check if all lengths are equal to expected_length
    if all(l == expected_length for l in tuple_lengths):
        return 'All tuples have same length'
    else:
        return 'All tuples do not have same length'