def minimum_Length(s: str) -> int:
    if not s:
        return 0
    char_counts = {}
    for ch in s:
        char_counts[ch] = char_counts.get(ch, 0) + 1
    max_count = max(char_counts.values())
    return len(s) - max_count