def sort_on_occurence(lst):
    from collections import Counter
    counts = Counter(item[0] for item in lst)
    sorted_items = sorted(lst, key=lambda x: (-counts[x[0]], x))
    result = []
    for key, group in sorted(sorted_items, key=lambda x: x[0]):
        # Group by first element
        groups = {}
        for i, item in enumerate(sorted_items):
            k = item[0]
            if k not in groups:
                groups[k] = []
            groups[k].append(item)
        for k in sorted(groups.keys()):
            grp = groups[k]
            sorted_grp = sorted(grp, key=lambda x: x)
            extended = []
            for item in sorted_grp:
                if isinstance(item, tuple):
                    extended.extend(list(item))
                else:
                    extended.append(item)
            result.append(extended)
    return result

assert sort_on_occurence([(1, 'Jake'), (2, 'Bob'), (1, 'Cara')]) == [(1, 'Jake', 'Cara', 2), (2, 'Bob', 1)]
assert sort_on_occurence([('b', 'ball'), ('a', 'arm'), ('b', 'b'), ('a', 'ant')]) == [('b', 'ball', 'b', 2), ('a', 'arm', 'ant', 2)]
assert sort_on_occurence([(2, 'Mark'), (3, 'Maze'), (2, 'Sara')]) == [(2, 'Mark', 'Sara', 2), (3, 'Maze', 1)]