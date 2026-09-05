def find_Sum(arr, k):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    total_sum = 0
    for num, count in counts.items():
        if count > 1:
            total_sum += num * count
    return total_sum