def extract_missing(intervals, start, end):
    result = []
    normalized = []
    for a, b in intervals:
        if a <= b:
            normalized.append((a, b))
        else:
            normalized.append((b, a))

    normalized.sort(key=lambda x: x[0])

    current = start
    for low, high in normalized:
        if low > current:
            result.append((current, low))
        current = max(current, high)

    if current <= end:
        result.append((current, end + 1))

    return result