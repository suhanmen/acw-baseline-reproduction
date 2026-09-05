def replace_list(lst, replacement):
    if not lst:  # Handle empty list case
        return replacement[:] if replacement else []
    last_index = len(lst) - 1
    lst[last_index] = replacement[0]
    return lst