def is_samepatterns(patterns, values):
    if len(patterns) != len(values):
        return False
    if not patterns and not values:
        return True
    if not patterns or not values:
        return False
    pattern_map = {}
    for pattern in patterns:
        if pattern not in pattern_map:
            pattern_map[pattern] = len(pattern_map) + 1
    for p, v in zip(patterns, values):
        if pattern_map.get(p, 0) != v:
            return False
    return True