def max_occurrences(lst):
    from collections import Counter
    counts = Counter(lst)
    max_count = max(counts.values())
    max_items = [item for item, count in counts.items() if count == max_count]
    return max_items[0] if len(max_items) > 1 else max_items[0]

# Test cases
assert max_occurrences([1,2,3,1,2,3,12,4,2]) ==  2
assert max_occurrences([1,2,6,7,0,1,0,1,0]) == 1,0
assert max_occurrences([1,2,3,1,2,4,1]) == 1