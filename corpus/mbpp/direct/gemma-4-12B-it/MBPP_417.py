def group_tuples(data):
    """
    Groups tuples that have the same first element.
    The first element is kept once, followed by all subsequent elements 
    from tuples sharing that first element.
    """
    groups = {}
    # To maintain the order of appearance of first elements
    order = []

    for item in data:
        first = item[0]
        rest = item[1:]
        if first not in groups:
            groups[first] = [first]
            order.append(first)
        groups[first].extend(rest)

    return [tuple(groups[key]) for key in order]