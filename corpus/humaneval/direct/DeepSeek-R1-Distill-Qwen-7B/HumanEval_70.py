def strange_sort_list(lst):
    if not lst:
        return []
    sorted_lst = sorted(lst)
    result = []
    take_min = True
    while sorted_lst:
        if take_min:
            result.append(sorted_lst.pop(0))
        else:
            result.append(sorted_lst.pop())
            sorted_lst.sort(reverse=True)  # Re-sort after reversing to handle next steps correctly
        take_min = not take_min
    return result