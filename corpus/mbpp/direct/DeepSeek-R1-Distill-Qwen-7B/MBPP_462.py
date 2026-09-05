def combinations_list(elements):
    if not elements:
        return [[]]
    current = elements[0]
    rest = elements[1:]
    without_current = combinations_list(rest)
    with_current = [[current] + comb for comb in combinations_list(rest)]
    return without_current + with_current