def colon_tuplex(t, i, x):
    lst = list(t)
    lst.insert(i, [x])
    return tuple(lst)