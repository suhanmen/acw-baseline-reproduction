def search(lst):
    if not lst:
        return -1

    frequency = {}
    for num in lst:
        if num > 0:
            frequency[num] = frequency.get(num, 0) + 1

    candidates = []
    for num in frequency:
        if frequency[num] >= num:
            candidates.append(num)

    return max(candidates) if candidates else -1