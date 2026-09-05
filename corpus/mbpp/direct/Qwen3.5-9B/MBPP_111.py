def common_in_nested_lists(nested_lists):
    from collections import Counter

    if not nested_lists:
        return []

    counter = Counter()
    for lst in nested_lists:
        counter.update(lst)

    return sorted([x for x, count in counter.items() if count == len(nested_lists)])