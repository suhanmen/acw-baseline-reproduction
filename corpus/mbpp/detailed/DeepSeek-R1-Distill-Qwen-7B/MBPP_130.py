def max_occurrences(lst):
    if not lst:
        return "The list is empty"

    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1

    max_freq = max(frequency.values())
    max_items = [item for item, count in frequency.items() if count == max_freq]

    for item in lst:
        if item in max_items:
            return (item, max_freq)

    return (lst[0], 1)