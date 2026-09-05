def check_k_elements(tuples_list, k):
    for t in tuples_list:
        if len(t) != k:
            return False
    return True