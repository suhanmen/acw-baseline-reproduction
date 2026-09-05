def rearange_string(s):
    from collections import Counter

    count = Counter(s)
    max_count = max(count.values())
    n = len(s)

    if max_count > (n + 1) // 2:
        return None  # Cannot be rearranged

    result = []
    last_char = None
    count_to_use = {}
    total = n
    chars_to_add = list(count.keys())
    idx = 0

    for _ in range(n):
        best_char = None
        for c in chars_to_add:
            if count[c] > 0 and c != last_char:
                # Prefer the most frequent remaining character
                if count[c] > best_count or best_count is None:
                    best_count = count[c]
                    best_char = c

        if best_char is None:
            # Fallback if no valid char found (shouldn't happen if valid)
            for c in chars_to_add:
                if count[c] > 0:
                    best_char = c
                    break

        result.append(best_char)
        count[best_char] -= 1
        last_char = best_char

    return ''.join(result)