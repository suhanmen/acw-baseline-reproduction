def count_rectangles(r):
    if not isinstance(r, int) or r < 0:
        return 0
    if r == 0:
        return 0
    diameter_squared = (2 * r) ** 2
    count = 0
    for a in range(r + 1):
        max_b = int((diameter_squared - a * a) ** 0.5)
        max_b = min(max_b, r)
        count += max_b + 1
    return count