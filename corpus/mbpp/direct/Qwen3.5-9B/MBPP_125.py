def find_length(s: str, n: int) -> int:
    max_diff = 0
    current_diff = 0
    min_diff = 0

    for ch in s:
        # Treat '0' as +1 and '1' as -1
        if ch == '0':
            current_diff += 1
        else:
            current_diff -= 1

        max_diff = max(max_diff, current_diff - min_diff)
        if current_diff < min_diff:
            min_diff = current_diff

    return max_diff