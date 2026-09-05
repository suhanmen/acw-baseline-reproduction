def replace_list(lst, new_list):
    if not lst:
        return new_list[:]
    return lst[:-1] + new_list