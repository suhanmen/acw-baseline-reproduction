def extract_missing(intervals, start, end):
    def is_between(x, y):
        return start <= x < y <= end

    result = []
    prev = start - 1

    for interval in intervals:
        if is_between(interval[0], interval[1]):
            result.append((start, interval[0]))
            result.append((interval[1], end))
        else:
            for x in interval:
                result.append((start, x))
                result.append((x, end))
        prev = interval[1]

    if prev < end:
        result.append((prev + 1, end))

    result = list(set(result))
    result.sort()

    return [x for x in result if x[0] <= x[1]]