def index_minimum(lst):
    if not lst:
        return None
    min_value = lst[0][1]
    min_index = 0
    for index, tuple_ in enumerate(lst[1:], start=1):
        if tuple_[1] < min_value:
            min_value = tuple_[1]
            min_index = index
    return lst[min_index][0]