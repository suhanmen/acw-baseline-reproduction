def min_Operations(a: int, b: int) -> int:
    if a == b:
        return 0
    if a <= 0 or b <= 0:
        return 0

    steps = 0
    smaller, larger = (a, b) if a < b else (b, a)

    while smaller < larger:
        if smaller == 0:
            return 0
        if smaller * 2 > larger:
            return -1

        ops_needed = (larger - smaller + smaller - 1) // (2 * smaller - 1)
        if ops_needed <= 0:
            return -1

        if smaller * (1 + 2 * (ops_needed - 1)) >= larger:
            steps += ops_needed - 1
            smaller *= (1 + 2 * (ops_needed - 1))
            if smaller >= larger:
                return -1
            return steps + 1

        steps += 1
        smaller *= 2

    return -1

assert min_Operations(2, 4) == 1
assert min_Operations(4, 10) == 4
assert min_Operations(1, 4) == 3