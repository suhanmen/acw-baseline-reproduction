def recursive_list_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += recursive_list_sum(item)
        else:
            total += item
    return total