def get_max_occuring_char(s: str) -> str:
    if not s:
        raise ValueError("Input string must not be empty")

    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    max_char = max(counts, key=counts.get)
    return max_char