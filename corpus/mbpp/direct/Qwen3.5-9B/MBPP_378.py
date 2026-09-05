def move_first(lst):
    if len(lst) == 0:
        return lst
    return [lst[-1]] + lst[:-1]