def check_Consecutive(lst):
    if len(lst) == 0:
        return False
    sorted_lst = sorted(lst)
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] - sorted_lst[i-1] != 1:
            return False
    return True