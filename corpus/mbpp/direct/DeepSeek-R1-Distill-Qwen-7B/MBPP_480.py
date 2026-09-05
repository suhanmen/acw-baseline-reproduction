def get_max_occuring_char(s):
    from collections import Counter
    counts = Counter(s)
    max_count = max(counts.values())
    max_chars = [char for char, cnt in counts.items() if cnt == max_count]
    return max_chars[0]