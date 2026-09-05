def check_subset_list(a_list, b_list):
    if not a_list and not b_list:
        return True
    if not a_list or not b_list:
        return False

    a_structure = [type(x) for x in a_list]
    b_structure = [type(x) for x in b_list]

    if a_structure != b_structure:
        return False

    if all(isinstance(elem, list) for elem in a_list):
        a_flat = []
        b_flat = []
        for sub in a_list:
            a_flat.extend(sub)
        for sub in b_list:
            b_flat.extend(sub)
        return set(a_flat).issubset(set(b_flat))
    else:
        return set(a_list) <= set(b_list)