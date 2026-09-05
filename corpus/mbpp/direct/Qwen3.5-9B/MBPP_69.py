def is_sublist(main_list, sublist):
    if not sublist:
        return True
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i + len(sublist)] == sublist:
            return True
    return False