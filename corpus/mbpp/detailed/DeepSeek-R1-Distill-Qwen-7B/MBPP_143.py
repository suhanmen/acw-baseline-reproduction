def find_lists(t):
    list_count = 0
    for element in t:
        if isinstance(element, list):
            list_count += 1
    return list_count