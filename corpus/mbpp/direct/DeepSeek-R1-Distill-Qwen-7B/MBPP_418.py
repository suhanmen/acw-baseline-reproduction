def Find_Max(lst):
    max_length = 0
    max_list = []
    for sublist in lst:
        current_length = len(sublist)
        if current_length > max_length:
            max_length = current_length
            max_list = sublist.copy()
    return max_list