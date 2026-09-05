from typing import List, Tuple

def max_difference(pairs: List[Tuple[int, int]]) -> int:
    if not pairs:
        return 0
    max_diff = 0
    for a, b in pairs:
        diff = abs(a - b)
        if diff > max_diff:
            max_diff = diff
    return max_diff