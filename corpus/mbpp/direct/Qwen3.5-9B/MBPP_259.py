def maximize_elements(tuple1, tuple2):
    result = ()
    for t1 in tuple1:
        t2 = None
        for t in tuple2:
            if t2 is None or t[0] > t2[0] or (t[0] == t2[0] and t[1] > t2[1]):
                t2 = t
        new_t = tuple(max(t1[0], t2[0]) if t2 else t1[0], max(t1[1], t2[1]) if t2 else t1[1])
        result = result + (new_t,)
    return result