def get_equal(tuples_list, expected_length):
    if not tuples_list:
        return 'All tuples have same length' if not tuples_list else 'All tuples have same length'
    first_length = len(tuples_list[0])
    for tup in tuples_list:
        if len(tup) != first_length:
            return 'All tuples do not have same length'
    return 'All tuples have same length'