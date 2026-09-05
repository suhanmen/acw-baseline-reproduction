def combinations_colors(colors, k):
    from itertools import product

    results = []
    # Sort to ensure deterministic order matching the test cases
    colors = sorted(colors)

    # Generate all combinations with repetition of length k
    for p in product(colors, repeat=k):
        results.append(tuple(p))

    return results