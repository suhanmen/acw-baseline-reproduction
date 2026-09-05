def remove_replica(t):
    from collections import Counter
    counts = Counter(t)
    result = []
    for x in t:
        if counts[x] > 1:
            if counts[x] == 1:  # Already processed and removed from count in iteration logic? No, we just mark.
                # This logic is flawed. Let's re-think: we need to know if this occurrence is the first.
                pass
        # Correct approach: iterate and decide based on current remaining count including self
        # But we can't modify dict during iteration easily for "first occurrence".
        # Better: count all, then iterate. If count > 1, it's a duplicate candidate.
        # But we only replace if it's NOT the first occurrence? 
        # Looking at example 1: (1, 1, 4, 4, 4, 5, 5, 6, 7, 7) -> (1, 'MSP', 4, 'MSP', 'MSP', 5, 'MSP', 6, 7, 'MSP')
        # 1 appears twice: first kept, second replaced.
        # 4 appears three times: first kept, next two replaced.
        # 5 appears twice: first kept, second replaced.
        # 6 appears once: kept.
        # 7 appears twice: first kept, second replaced.
        # So rule: If element count > 1, keep the first occurrence, replace all subsequent occurrences.
        pass
    # Re-implement cleanly
    counts = Counter(t)
    result = []
    # We need to track which instances we've seen for each number.
    seen = {}
    for x in t:
        if counts[x] > 1:
            if x not in seen:
                seen[x] = 0
            seen[x] += 1
            if seen[x] == 1:
                result.append(x)
            else:
                result.append('MSP')
        else:
            result.append(x)
    return tuple(result)