def assign_freq(tuples):
    from collections import Counter

    if not tuples:
        return '[]'

    counted = Counter(tuple(item) for item in tuples)
    result = []
    for t in tuples:
        key = tuple(t)
        count = counted[key]
        if isinstance(t, tuple):
            new_tuple = t + (count,)
        else:
            new_tuple = (t, count)
        result.append(new_tuple)

    return str(result)