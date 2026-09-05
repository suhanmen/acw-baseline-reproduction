def find_Sum(arr, k):
    from collections import Counter
    counts = Counter(arr)
    total = 0
    for num, count in counts.items():
        if count > 1:
            total += num * (count - 1)
    return total