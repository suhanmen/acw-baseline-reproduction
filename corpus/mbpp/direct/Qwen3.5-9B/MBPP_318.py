def max_volume(n: int) -> int:
    if n <= 3:
        return 0
    # Optimal cuboid dimensions are as close to each other as possible.
    # Let dimensions be a, b, c such that a + b + c = n.
    # We try integer values for a from 1 to n//3, then b from a to (n-a)//2,
    # and c is determined as n - a - b.
    for a in range(1, n // 3 + 1):
        for b in range(a, (n - a) // 2 + 1):
            c = n - a - b
            if c < b:
                continue
            volume = a * b * c
            return volume
    return 0