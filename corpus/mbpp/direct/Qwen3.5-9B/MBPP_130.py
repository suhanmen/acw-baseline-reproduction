from collections import Counter

def max_occurrences(lst):
    if not lst:
        return None
    counts = Counter(lst)
    max_item = max(counts, key=counts.get)
    return (max_item, counts[max_item])