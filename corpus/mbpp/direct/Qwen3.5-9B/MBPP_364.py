def min_flip_to_make_string_alternate(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    # Option 1: Target starts with '0' -> "010101..."
    flips_if_starts_with_0 = 0
    for i in range(n):
        expected = str(i % 2)
        if s[i] != expected:
            flips_if_starts_with_0 += 1

    # Option 2: Target starts with '1' -> "101010..."
    flips_if_starts_with_1 = 0
    for i in range(n):
        expected = str(1 - i % 2)
        if s[i] != expected:
            flips_if_starts_with_1 += 1

    return min(flips_if_starts_with_0, flips_if_starts_with_1)