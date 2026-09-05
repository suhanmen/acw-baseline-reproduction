def min_length_list(arr):
    if not arr:
        return (0, ())
    min_len = len(arr[0])
    min_list = arr[0]
    for lst in arr[1:]:
        if len(lst) < min_len:
            min_len = len(lst)
            min_list = lst
        elif len(lst) == min_len:
            if tuple(lst) < tuple(min_list):
                min_list = lst
    return (min_len, tuple(min_list))