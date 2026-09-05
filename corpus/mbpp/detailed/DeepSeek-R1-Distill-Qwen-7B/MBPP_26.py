def check_k_elements(tuples_list, k):
    # Validate the input
    if not isinstance(tuples_list, list) or not isinstance(k, int) or k <= 0:
        return False

    # Check if the list is empty
    if not tuples_list:
        return False

    # Check each tuple's length
    for tup in tuples_list:
        if not isinstance(tup, tuple) or len(tup) != k:
            return False

    # All checks passed
    return True