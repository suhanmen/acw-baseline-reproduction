def move_first(lst):
    if not lst:
        return []
    if len(lst) == 1:
        return lst.copy()  # Return a copy to avoid mutation of the original list
    last_element = lst[-1]
    rest_of_list = lst[:-1]
    return [last_element] + rest_of_list