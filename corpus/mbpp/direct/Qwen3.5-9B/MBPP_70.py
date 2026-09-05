def get_equal(tuples_list, length):
    if not all(len(t) == length for t in tuples_list):
        return 'All tuples do not have same length'
    return 'All tuples have same length'