def check_k_elements(tuple_list, k):
    for tup in tuple_list:
        if len(tup) == k:
            return True
    return False