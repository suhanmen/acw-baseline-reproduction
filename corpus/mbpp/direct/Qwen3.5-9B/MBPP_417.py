def group_tuples(tuples):
    from collections import defaultdict
    groups = defaultdict(list)
    for t in tuples:
        groups[t[0]].append(t)
    result = []
    for k, group in groups.items():
        if len(group) == 1:
            result.append(group[0])
        else:
            new_t = (k,) + tuple(x[1] for x in group)
            result.append(new_t)
    return result