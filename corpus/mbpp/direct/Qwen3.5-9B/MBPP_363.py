def add_K_element(tuples_list, k):
    return [tuple(x + k for x in t) for t in tuples_list]