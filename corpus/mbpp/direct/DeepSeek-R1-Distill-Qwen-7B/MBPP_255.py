def combinations_colors(colors, n):
    if n == 0:
        return [[]]
    if n == 1:
        return [(color,) for color in colors]
    combinations = []
    for color in colors:
        for prev in combinations_colors(colors, n - 1):
            combinations.append((color,) + prev)
    return combinations