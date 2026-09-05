def min_length_list(lst):
    return (min(len(sub) for sub in lst), [sub for sub in lst if len(sub) == min(len(inner) for inner in lst)][0])