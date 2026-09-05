def first_Element(arr, k, n):
    counts = {}
    first_occurrence = {}
    for index, value in enumerate(arr):
        if value in counts:
            counts[value] += 1
            if value not in first_occurrence:
                first_occurrence[value] = index
        else:
            counts[value] = 1
            first_occurrence[value] = index
    for value in arr:
        if counts[value] == n:
            return value
    return None