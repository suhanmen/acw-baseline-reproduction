def max_occurrences(lst):
    from collections import defaultdict

    count = defaultdict(int)
    for item in lst:
        count[item] += 1

    max_freq = max(count.values())

    for key, value in count.items():
        if value == max_freq:
            return (key, value)

    return (None, 0)