def extract_freq(lst):
    counts = {}
    order = []
    for tup in lst:
        if tup not in counts:
            counts[tup] = 1
            order.append(tup)
        else:
            counts[tup] += 1

    result = 0
    for tup in order:
        result += counts[tup]

    return result